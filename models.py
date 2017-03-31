"""
SWEatshop Database Models

Note: Pylint does not work well with SQLAlchemy since it is
      dynamically generated
"""
# pylint: disable=E1101
# pylint: disable=too-many-arguments
# pylint: disable=too-few-public-methods
# pylint: disable=too-many-instance-attributes
# pylint: disable=invalid-name

from enum import Enum
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config

APP = Flask(__name__)
APP.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
APP.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(APP)


class Ownership(Enum):

    """IPO or not"""
    PUBLIC = 'Public'
    PRIVATE = 'Private'

investment = db.Table(
    'investment',
    db.Column('company_id', db.Integer, db.ForeignKey('company.idnum')),
    db.Column('investor_id', db.Integer, db.ForeignKey('investor.idnum')))

school_investment = db.Table(
    'school_investment',
    db.Column('school_id', db.Integer, db.ForeignKey('school.idnum')),
    db.Column('investor_id', db.Integer, db.ForeignKey('investor.idnum')))

employment = db.Table(
    'employment',
    db.Column('person_id', db.Integer, db.ForeignKey('person.idnum')),
    db.Column('company_id', db.Integer, db.ForeignKey('company.idnum')))

education = db.Table(
    'education',
    db.Column('person_id', db.Integer, db.ForeignKey('person.idnum')),
    db.Column('school_id', db.Integer, db.ForeignKey('school.idnum')))

company_category = db.Table(
    'company_category',
    db.Column('category_id', db.Integer, db.ForeignKey('category.idnum')),
    db.Column('company_id', db.Integer, db.ForeignKey('company.idnum')))

investor_category = db.Table(
    'investor_category',
    db.Column('category_id', db.Integer, db.ForeignKey('category.idnum')),
    db.Column('investor_id', db.Integer, db.ForeignKey('investor.idnum')))


class Person(db.Model):

    """Person Model"""
    __tablename__ = 'person'
    idnum = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    title = db.Column(db.String(200), nullable=True)
    location = db.Column(db.String(500), nullable=True)
    dob = db.Column(db.DateTime, nullable=True)
    image_url = db.Column(db.String(512), nullable=True)
    website = db.Column(db.String(512), nullable=True)
    companies = db.relationship('Company', secondary=employment,
                                backref=db.backref('employees', lazy='dynamic'))
    schools = db.relationship('School', secondary=education,
                              backref=db.backref('alumni', lazy='dynamic'))
    crunch_id = db.Column(db.String(25), nullable=True)
    description = db.Column(db.String(10000), nullable=True)

    def __init__(self, name, title, location, dob, image_url, website):
        """Initializes a Person, pass in dob as datetime object"""
        self.name = name
        self.title = title
        self.location = location
        self.dob = dob
        self.image_url = image_url
        self.website = website

    def __repr__(self):
        return '<Person %r>' % self.name

    def get_all_rows(self):
        """Get all person rows"""
        return self.query.all()


class Company(db.Model):

    """Company Model"""
    __tablename__ = 'company'
    idnum = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    location = db.Column(db.String(500), nullable=True)
    ownership_type = db.Column(db.Enum(Ownership), nullable=True)
    funding = db.Column(db.Integer, nullable=True)
    description = db.Column(db.String(10000), nullable=True)
    ceo_id = db.Column(
        db.Integer, db.ForeignKey('person.idnum'), nullable=True)
    image_url = db.Column(db.String(512), nullable=True)
    size = db.Column(db.Integer, nullable=True)
    website = db.Column(db.String(512), nullable=True)
    investors = db.relationship('Investor', secondary=investment,
                                backref=db.backref('companies', lazy='dynamic'))
    crunch_id = db.Column(db.String(25), nullable=True)

    def __init__(self, name, location, ownership_type, funding, description,
                 ceo_id, image_url, size, website):
        """Initializes Company, ceo as foreign key and ownership as enum"""
        self.name = name
        self.location = location
        self.ownership_type = ownership_type
        self.funding = funding
        self.description = description
        self.ceo_id = ceo_id
        self.image_url = image_url
        self.size = size
        self.website = website

    def __repr__(self):
        return '<Company %r>' % self.name

    def get_all_rows(self):
        """Get all company rows"""
        return self.query.all()


class School(db.Model):

    """School Model"""
    __tablename__ = 'school'
    idnum = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    location = db.Column(db.String(50), nullable=True)
    description = db.Column(db.String(350), nullable=True)
    size = db.Column(db.Integer, nullable=True)
    image_url = db.Column(db.String(512), nullable=True)
    website = db.Column(db.String(512), nullable=True)
    investors = db.relationship('Investor', secondary=school_investment,
                                backref=db.backref('schools', lazy='dynamic'))

    def __init__(self, name, location, description, image_url, size, website):
        self.name = name
        self.location = location
        self.description = description
        self.image_url = image_url
        self.size = size
        self.website = website

    def __repr__(self):
        return '<School %r>' % self.name

    def get_all_rows(self):
        """Get all school rows"""
        return self.query.all()


class Investor(db.Model):

    """Investor Model"""
    __tablename__ = 'investor'
    idnum = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    location = db.Column(db.String(50), nullable=True)
    funding = db.Column(db.Integer, nullable=True)
    description = db.Column(db.String(350), nullable=True)
    image_url = db.Column(db.String(512), nullable=True)
    website = db.Column(db.String(512), nullable=True)

    def __init__(self, name, location, funding, description, image_url, website):
        self.name = name
        self.location = location
        self.funding = funding
        self.description = description
        self.image_url = image_url
        self.website = website

    def __repr__(self):
        return '<Investor %r>' % self.name

    def get_all_rows(self):
        """Get all investor rows"""
        return self.query.all()


class Category(db.Model):

    """Categories"""
    __tablename__ = 'category'
    idnum = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Category %r>' % self.name

    def get_all_rows(self):
        """Get all category rows"""
        return self.query.all()
