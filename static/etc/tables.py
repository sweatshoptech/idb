#!flask/bin/python

"""Grids used in HTML pages"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_table import Table, Col, DateCol
import models


class CompanyTable(Table):
    idnum = Col('ID')
    name = Col('Company')
    website = Col('Website')
    ownership_type = Col('Ownership')
    funding = Col('Funding')
    ceo_id = Col('CEO')
    size = Col('Size')
    location = Col('Location')

    def get_tr_attrs(self, item):
        href_text = 'company/{0}'.format(item.idnum)
        return {'class': 'clickable-row', 'data-href': href_text}


class SchoolTable(Table):
    idnum = Col('ID')
    name = Col('School')
    website = Col('Website')
    size = Col('Size')
    location = Col('Location')

    def get_tr_attrs(self, item):
        href_text = 'school/{0}'.format(item.idnum)
        return {'class': 'clickable-row', 'data-href': href_text}


class InvestorTable(Table):
    idnum = Col('ID')
    name = Col('Investor')
    website = Col('Website')
    funding = Col('Funding')
    location = Col('Location')

    def get_tr_attrs(self, item):
        href_text = 'investor/{0}'.format(item.idnum)
        return {'class': 'clickable-row', 'data-href': href_text}


class PersonTable(Table):
    idnum = Col('ID')
    name = Col('Person')
    website = Col('Website')
    title = Col('Title')
    dob = DateCol('Date of Birth', date_format="medium")
    location = Col('Location')

    def get_tr_attrs(self, item):
        href_text = 'person/{0}'.format(item.idnum)
        return {'class': 'clickable-row', 'data-href': href_text}


table_mappings = {models.Company: CompanyTable, models.Person:
                  PersonTable, models.Investor: InvestorTable, models.School: SchoolTable}


def get_table_html(model):
    companies = model.query.all()
    table = table_mappings[model](companies)
    return table.__html__()
