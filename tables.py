#!flask/bin/python

"""Grids used in HTML pages"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_table import Table, Col
import models


class CompanyTable(Table):
    name = Col('Company')
    website = Col('Website')
    ownership_type = Col('Ownership')
    funding = Col('Funding')
    ceo_id = Col('CEO')
    size = Col('Size')
    location = Col('Location')


class SchoolTable(Table):
    name = Col('School')
    website = Col('Website')
    size = Col('Size')
    location = Col('Location')


class InvestorTable(Table):
    name = Col('Investor')
    website = Col('Website')
    location = Col('Location')


class PersonTable(Table):
    name = Col('Person')
    website = Col('Website')
    title = Col('Title')
    dob = Col('Date of Birth')
    location = Col('Location')

table_mappings = {models.Company: CompanyTable, models.Person:
                  PersonTable, models.Investor: InvestorTable, models.School: SchoolTable}


def get_table_html(model):
    companies = model.query.all()
    table = table_mappings[model](companies)
    return table.__html__()
