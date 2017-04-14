#!flask/bin/python

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_paginate import Pagination, get_page_args
import models
import subprocess
import tests
import flask_restless
import formatters
import re

app = Flask(__name__)
manager = flask_restless.APIManager(app, flask_sqlalchemy_db=models.db)
manager.create_api(models.Person, methods=['GET'])
manager.create_api(models.Company, methods=['GET'])
manager.create_api(models.Investor, methods=['GET'])
manager.create_api(models.School, methods=['GET'])


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
@app.route('/index.html', methods=['GET', 'POST'])
def home_page():
    return render_template('index.html')


@app.route('/about')
@app.route('/about.html')
def about():
    return render_template('about.html')


@app.route('/companies/page/<int:page>')
@app.route('/companies/', defaults={'page': 1})
@app.route('/companies.html/', defaults={'page': 1})
def companies(page):
    # Get page data
    page, per_page, offset = get_page_args()

    # Get sort data
    sortBy = request.args.get('sort', type=str, default='name')
    sortBy = getattr(models.Company, sortBy or 'name')
    sortOrder = request.args.get('order', type=str, default='asc')
    sortBy = sortBy.desc() if sortOrder == 'desc' else sortBy
    companies = models.Company.query.order_by(sortBy)

    # Get filter data
    ownership = request.args.get('ownership-type', type=str, default=None)
    if ownership:
        companies = companies.filter_by(ownership_type=ownership)
    country = request.args.get('country', type=str, default=None)
    if country:
        companies = companies.filter_by(country=country)

    total = len(companies.all())
    companies = companies.offset(offset).limit(per_page).all()

    # Render with pagination
    pagination = Pagination(
        page=page, per_page=per_page, total=total, record_name='companies')
    return render_template('companies.html', companies=companies, page=page,
                           per_page=per_page, pagination=pagination)


@app.route('/company/<int:company_id>')
def company_template(company_id):
    company = models.Company.query.get(company_id)
    ceo = models.Person.query.get(company.ceo_id) if company.ceo_id else None
    investors = company.investors if company.investors else []
    return render_template('company_template.html', company=company, ceo=ceo,
                           employees=company.employees, investors=investors,
                           description=formatters.markdown_remove(company.description))


@app.route('/person/<int:person_id>')
def person_template(person_id):
    person = models.Person.query.get(person_id)
    companies = person.companies
    schools = person.schools
    return render_template('person_template.html', person=person,
                           companies=companies, schools=schools,
                           description=formatters.markdown_remove(person.description))


@app.route('/school/<int:school_id>')
def school_template(school_id):
    school = models.School.query.get(school_id)
    alum = school.alumni.all()
    investors = school.investors if school.investors else []
    return render_template('school_template.html', school=school, alum=alum,
                           investors=investors,
                           description=formatters.markdown_remove(school.description))


@app.route('/investor/<int:investor_id>')
def investor_template(investor_id):
    investor = models.Investor.query.get(investor_id)
    companies = investor.companies.all()
    companies = companies if companies else []
    schools = investor.schools.all()
    return render_template('investor_template.html', investor=investor,
                           companies=companies, schools=schools,
                           description=formatters.markdown_remove(investor.description))


@app.route('/schools/page/<int:page>')
@app.route('/schools/', defaults={'page': 1})
@app.route('/schools.html/', defaults={'page': 1})
def schools(page):
    # Get page data
    page, per_page, offset = get_page_args()

    # Get sort data
    sortBy = request.args.get('sort', type=str, default='name')
    sortBy = getattr(models.School, sortBy or 'name')
    sortOrder = request.args.get('order', type=str, default='asc')
    sortBy = sortBy.desc() if sortOrder == 'desc' else sortBy
    schools = models.School.query.order_by(sortBy)

    # Get filter data
    country = request.args.get('country', type=str, default=None)
    if country:
        schools = schools.filter_by(country=country)

    total = len(schools.all())
    schools = schools.offset(offset).limit(per_page).all()

    # Render with pagination
    pagination = Pagination(
        page=page, per_page=per_page, total=total, record_name='schools')
    return render_template('schools.html', schools=schools, page=page,
                           per_page=per_page, pagination=pagination)


@app.route('/investors/page/<int:page>')
@app.route('/investors/', defaults={'page': 1})
@app.route('/investors.html/', defaults={'page': 1})
def investors(page):
    # Get page data
    page, per_page, offset = get_page_args()

    # Get sort data
    sortBy = request.args.get('sort', type=str, default='name')
    sortBy = getattr(models.Investor, sortBy or 'name')
    sortOrder = request.args.get('order', type=str, default='asc')
    sortBy = sortBy.desc() if sortOrder == 'desc' else sortBy
    investors = models.Investor.query.order_by(sortBy)

    # Get filter data
    country = request.args.get('country', type=str, default=None)
    if country:
        investors = investors.filter_by(country=country)

    total = len(investors.all())
    investors = investors.offset(offset).limit(per_page).all()

    # Render with pagination
    pagination = Pagination(
        page=page, per_page=per_page, total=total, record_name='investors')
    return render_template('investors.html', investors=investors, page=page,
                           per_page=per_page, pagination=pagination)


@app.route('/people/page/<int:page>')
@app.route('/people/', defaults={'page': 1})
@app.route('/people.html/', defaults={'page': 1})
def people(page):
    # Get page data
    page, per_page, offset = get_page_args()

    # Get sort data
    sortBy = request.args.get('sort', type=str, default='name')
    sortBy = getattr(models.Person, sortBy or 'name')
    sortOrder = request.args.get('order', type=str, default='asc')
    sortBy = sortBy.desc() if sortOrder == 'desc' else sortBy
    people = models.Person.query.order_by(sortBy)

    # Get filter data
    title = request.args.get('job-type', type=str, default=None)
    if title:
        people = people.filter(
            models.Person.title.ilike("%{0}%".format(title)))
    country = request.args.get('country', type=str, default=None)
    if country:
        people = people.filter_by(country=country)

    total = len(people.all())
    people = people.offset(offset).limit(per_page).all()

    # Render with pagination
    pagination = Pagination(
        page=page, per_page=per_page, total=total, record_name='people')
    return render_template('people.html', people=people, page=page,
                           per_page=per_page, pagination=pagination)


@app.route('/report')
@app.route('/report.html')
def report():
    return render_template('report/report.html')


@app.route('/report/<subpage>')
def reportsub(subpage):
    return render_template('report/{0}'.format(subpage))


@app.route('/run-tests')
def run_tests():
    """
    Run tests and output results with coverage
    """
    try:
        tests = subprocess.check_output(
            ['python', '-W', 'ignore', '/home/ubuntu/idb/tests.py'],
            stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError, e:
        tests = e.output
    with open('/home/ubuntu/idb/coverage.out') as coverage:
        tests = tests + coverage.read()
    testout = tests.replace('\n', '<br/>')
    return render_template('TestIDB.html', test=testout)


def get_search_results(query, model, rec, template):
    """
    Standard template to return search results for models
    """
    # Get page data
    page, per_page, offset = get_page_args()

    with models.APP.app_context():
        results = model.query.whoosh_search(
            query, or_=True, like=True)
    
    total = len(results.all())
    orgs = results.offset(offset).limit(per_page).all()
    pagination = Pagination(
        page=page, per_page=per_page, total=total, record_name='{0} found for <b>"{1}"</b>'.format(rec, query))

    return render_template(
        template, page=page, per_page=per_page, keyword=query,
                           pagination=pagination, results=orgs)


@app.route('/search/<query>/')
def search(query):
    """
    Search for keywords in all attributes of all tables
    """
    return search_people(query)


@app.route('/search/person/<query>/')
def search_people(query):
    """
    Search for keywords in all attributes of people
    """
    return get_search_results(query, models.Person, 'people', 'person_results.html')


@app.route('/search/company/<query>/')
def search_companies(query):
    """
    Search for keywords in all attributes of companies
    """
    return get_search_results(query, models.Company, 'companies', 'company_results.html')


@app.route('/search/investor/<query>/')
def search_investors(query):
    """
    Search for keywords in all attributes of investors
    """
    return get_search_results(query, models.Investor, 'investors', 'investor_results.html')

@app.route('/search/school/<query>/')
def search_schools(query):
    """
    Search for keywords in all attributes of schools
    """
    return get_search_results(query, models.School, 'schools', 'school_results.html')



@app.route('/visualization')
@app.route('/visualization.html')
def visualization():
    return render_template('visualization.html')


@app.context_processor
def utility_processor():
    def highlight_keys(text, keyword):
        pattern = re.compile('(' + keyword + ')', re.IGNORECASE)
        return pattern.sub('<b style="background-color: yellow; color: #333;">{0}</b>'.format(r'\1'), text) if text else None
    return dict(highlight_keys=highlight_keys)

if __name__ == '__main__':
    app.run()
