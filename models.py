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

from datetime import date
import getpass
from enum import Enum
import flask_whooshalchemyplus
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config

APP = Flask(__name__)
APP.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
APP.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
APP.config['TESTING'] = True
APP.config['WTF_CSRF_ENABLED'] = False

if getpass.getuser() != 'ubuntu':  # pragma: no cover
    APP.config['WHOOSH_BASE'] = '/home/ubuntu/idb/index-whoosh'

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
    country = db.Column(db.String(50), nullable=True)
    description = db.Column(db.String(10000), nullable=True)
    __searchable__ = ['name', 'title', 'location', 'website',
                      'companies', 'schools', 'country', 'description']

    def __init__(self, name, title, location, dob, image_url, website):
        """Initializes a Person, pass in dob as datetime object"""

        # Name not nullable
        assert name is not None and isinstance(name, str) and len(name) <= 50
        assert title is None or (isinstance(title, str) and len(title) <= 200)
        assert location is None or (
            isinstance(location, str) and len(name) <= 500)
        assert dob is None or isinstance(dob, date)
        assert image_url is None or (
            isinstance(image_url, str) and len(name) <= 512)
        assert website is None or (
            isinstance(website, str) and len(name) <= 512)

        self.name = name
        self.title = title
        self.location = location
        self.dob = dob
        self.image_url = image_url
        self.website = website

    def __repr__(self):
        return '<Person %s>' % self.name

    @classmethod
    def get_all_rows(cls):
        """Get all person rows"""
        return cls.query.all()


class Company(db.Model):

    """Company Model"""
    __tablename__ = 'company'
    idnum = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    location = db.Column(db.String(500), nullable=True)
    # ownership_type = db.Column(db.Enum(Ownership), nullable=True)
    ownership_type = db.Column(db.String(50), nullable=False)
    funding = db.Column(db.Integer, nullable=True)
    description = db.Column(db.String(10000), nullable=True)
    ceo_id = db.Column(
        db.Integer, db.ForeignKey('person.idnum'), nullable=True)
    image_url = db.Column(db.String(512), nullable=True)
    size = db.Column(db.Integer, nullable=True)
    website = db.Column(db.String(512), nullable=True)
    country = db.Column(db.String(50), nullable=True)
    investors = db.relationship('Investor', secondary=investment,
                                backref=db.backref('companies', lazy='dynamic'))
    crunch_id = db.Column(db.String(25), nullable=True)
    __searchable__ = ['name', 'location', 'ownership_type',
                      'funding', 'website', 'country', 'description', 'investors']

    def __init__(self, name, location, ownership_type, funding, description,
                 ceo_id, image_url, size, website):
        """Initializes Company, ceo as foreign key and ownership as enum"""

        # Name not nullable
        assert name is not None and isinstance(name, str) and len(name) <= 50

        assert location is None or (
            isinstance(location, str) and len(name) <= 500)
        assert funding is None or isinstance(funding, int)
        assert description is None or (
            isinstance(description, str) and len(description) <= 10000)
        assert ceo_id is None or isinstance(ceo_id, int)
        assert image_url is None or (
            isinstance(image_url, str) and len(image_url) <= 512)
        assert size is None or isinstance(size, int)
        assert website is None or (
            isinstance(website, str) and len(website) <= 512)

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
        return '<Company %s>' % self.name

    @classmethod
    def get_all_rows(cls):
        """Get all company rows"""
        return cls.query.all()


class School(db.Model):

    """School Model"""
    __tablename__ = 'school'
    idnum = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    location = db.Column(db.String(50), nullable=True)
    description = db.Column(db.String(10000), nullable=True)
    size = db.Column(db.Integer, nullable=True)
    image_url = db.Column(db.String(512), nullable=True)
    website = db.Column(db.String(512), nullable=True)
    country = db.Column(db.String(200), nullable=True)
    investors = db.relationship('Investor', secondary=school_investment,
                                backref=db.backref('schools', lazy='dynamic'))
    __searchable__ = [
        'name', 'location', 'website', 'country', 'investors', 'description']

    def __init__(self, name, location, description, image_url, size, website):
        """Initializes School"""

        # Name not nullable
        assert name is not None and isinstance(name, str) and len(name) <= 150
        assert location is None or (
            isinstance(location, str) and len(name) <= 50)
        assert description is None or (
            isinstance(description, str) and len(description) <= 10000)
        assert image_url is None or (
            isinstance(image_url, str) and len(image_url) <= 512)
        assert size is None or isinstance(size, int)
        assert website is None or (
            isinstance(website, str) and len(website) <= 512)

        self.name = name
        self.location = location
        self.description = description
        self.image_url = image_url
        self.size = size
        self.website = website

    def __repr__(self):
        return '<School %s>' % self.name

    @classmethod
    def get_all_rows(cls):
        """Get all school rows"""
        return cls.query.all()


class Investor(db.Model):

    """Investor Model"""
    __tablename__ = 'investor'
    idnum = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    location = db.Column(db.String(50), nullable=True)
    funding = db.Column(db.Integer, nullable=True)
    description = db.Column(db.String(10000), nullable=True)
    image_url = db.Column(db.String(512), nullable=True)
    country = db.Column(db.String(50), nullable=True)
    website = db.Column(db.String(512), nullable=True)
    __searchable__ = [
        'name', 'location', 'funding', 'website', 'country', 'description']

    def __init__(self, name, location, funding, description, image_url, website):
        """Initializes Investor"""

        # Name not nullable
        assert name is not None and isinstance(name, str) and len(name) <= 150
        assert location is None or (
            isinstance(location, str) and len(name) <= 50)
        assert funding is None or (isinstance(funding, int))
        assert description is None or(
            isinstance(description, str) and len(description) <= 10000)
        assert image_url is None or (
            isinstance(image_url, str) and len(image_url) <= 512)
        assert website is None or (
            isinstance(website, str) and len(website) <= 512)

        self.name = name
        self.location = location
        self.funding = funding
        self.description = description
        self.image_url = image_url
        self.website = website

    def __repr__(self):
        return '<Investor %s>' % self.name

    @classmethod
    def get_all_rows(cls):
        """Get all investor rows"""
        return cls.query.all()


class Category(db.Model):

    """Categories"""
    __tablename__ = 'category'
    idnum = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    def __init__(self, name):
        assert name is not None
        assert isinstance(name, str) and len(name) <= 50
        self.name = name

    def __repr__(self):
        return '<Category %s>' % self.name

    @classmethod
    def get_all_rows(cls):
        """Get all category rows"""
        return cls.query.all()

flask_whooshalchemyplus.init_app(APP)

if __name__ == "__main__":  # pragma: no cover
    with APP.app_context():
        flask_whooshalchemyplus.index_all(APP)
