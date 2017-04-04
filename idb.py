#!flask/bin/python

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import models
import subprocess
import tests

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
@app.route('/index.html', methods=['GET', 'POST'])
def home_page():
    return render_template('index.html')


@app.route('/about')
@app.route('/about.html')
def about():
    return render_template('about.html')


@app.route('/companies')
@app.route('/companies.html')
def companies():
    return render_template('companies.html', companies=models.Company.query.all())


@app.route('/company/<int:company_id>')
def company_template(company_id):
    company = models.Company.query.get(company_id)
    ceo = models.Person.query.get(company.ceo_id) if company.ceo_id else None
    investor = company.investors[0] if company.investors else None
    return render_template('company_template.html', company=company, ceo=ceo, investor=investor)


@app.route('/person/<int:person_id>')
def person_template(person_id):
    person = models.Person.query.get(person_id)
    companies = person.companies[0] if person.companies else None
    schools = person.schools[0] if person.schools else None
    return render_template('person_template.html', person=person, company=companies, school=schools)


@app.route('/school/<int:school_id>')
def school_template(school_id):
    school = models.School.query.get(school_id)
    alum = school.alumni.all()
    people = alum[0] if alum else None
    investors = school.investors[0] if person.investors else None
    return render_template('school_template.html', school=school, alum=people, investor=investors)


@app.route('/investor/<int:investor_id>')
def investor_template(investor_id):
    investor = models.Investor.query.get(investor_id)
    companies = investor.companies.all()[0]
    schools = investor.schools.all()[0]
    return render_template('investor_template.html', investor=investor, company=companies, school=schools)


@app.route('/schools')
@app.route('/schools.html')
def schools():
    return render_template('schools.html', schools=models.School.query.all())


@app.route('/investors')
@app.route('/investors.html')
def investors():
    return render_template('investors.html', investors=models.Investor.query.all())


@app.route('/people')
@app.route('/people.html')
def people():
    return render_template('people.html', people=models.Person.query.all())


@app.route('/report')
@app.route('/report.html')
def report():
    return render_template('report/report.html')


@app.route('/report/<subpage>')
def reportsub(subpage):
    return render_template('report/{0}'.format(subpage))


@app.route('/run-tests')
def run_tests():
    """    with open("tests.out", "w+") as fi:
        fi.write(tests.run_my_tests())
    """
    try:
        tests = subprocess.check_output(
            ['python', '-W', 'ignore', '/home/ubuntu/idb/tests.py'], stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError, e:
        tests = e.output
    testout = tests.replace('\n', '<br/>')
    return render_template('TestIDB.html', test=testout)


if __name__ == '__main__':
    app.run()
