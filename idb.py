#!flask/bin/python

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from application import db
from application.models import Data
from application.forms import EnterDBInfo, RetrieveDBInfo

app = Flask(__name__)
app.debug= True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://flask:SWEatshop@sweatshop.cvsgdbsefofi.us-east-1.rds.amazonaws.com/db1'
db = SQLAlchemy(app)
'''
class Company(db.Model):
    __table__ = db.Model.metadata.tables['COMPANY']

    def __repr__(self):
        return self.NAME
'''
@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
@app.route('/index.html', methods=['GET', 'POST'])
def home_page():
    #form1 = EnterDBInfo(request.form)
    #form2 = RetrieveDBInfo(request.form)
    return render_template('index.html')

@app.route('/about')
@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/companies')
@app.route('/companies.html')
def companies():
    return render_template('companies.html')

@app.route('/schools')
@app.route('/schools.html')
def schools():
    return render_template('schools.html')

@app.route('/investors')
@app.route('/investors.html')
def investors():
    return render_template('investors.html')

@app.route('/people')
@app.route('/people.html')
def people():
    return render_template('people.html')

@app.route('/implementation')
@app.route('/implementation.html')
def implementation():
    return render_template('implementation.html')

@app.route('/tester/<input_str>')
def tester(input_str):
    return str(db.Model.metadata.tables)#str(Company.query.get(1))



if __name__ == '__main__':
  app.run()
