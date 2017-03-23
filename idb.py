#!flask/bin/python

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import models
import tables

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
    return render_template('companies.html', companies=tables.get_table_html(models.Company))

@app.route('/company/<int:company_id>')
def company_template(company_id):
    company = models.Company.query.get(company_id)
    ceo = models.Person.query.get(company.ceo_id)
    investors = company.investors
    return render_template('company_template.html', company=company, ceo=ceo, investor=investors[0])

@app.route('/person/<int:person_id>')
def person_template(person_id):
    person = models.Person.query.get(person_id)
    companies = person.companies[0]
    schools = person.schools[0]
    return render_template('person_template.html', person=person, company=companies, school=schools)

@app.route('/school/<int:school_id>')
def school_template(school_id):
    school = models.School.query.get(school_id)
    people = school.alumni.all()[0]
    return render_template('school_template.html', school=school, alum=people)

@app.route('/investor/<int:investor_id>')
def investor_template(investor_id):
    investor = models.Investor.query.get(investor_id)
    companies = investor.companies.all()[0]
    return render_template('investor_template.html', investor=investor, company=companies)

@app.route('/schools')
@app.route('/schools.html')
def schools():
    return render_template('schools.html', schools=tables.get_table_html(models.School))

@app.route('/investors')
@app.route('/investors.html')
def investors():
    return render_template('investors.html', investors=tables.get_table_html(models.Investor))

@app.route('/people')
@app.route('/people.html')
def people():
    return render_template('people.html', people=tables.get_table_html(models.Person))

@app.route('/implementation')
@app.route('/implementation.html')
def report():
    return render_template('implementation.html')

if __name__ == '__main__':
  app.run()
