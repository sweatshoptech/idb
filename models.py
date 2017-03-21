"""
SWEatshop Database Models
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from enum import Enum

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://flask:SWEatshop@sweatshop.cvsgdbsefofi.us-east-1.rds.amazonaws.com:5432/db1'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

class Ownership(Enum):
    PUBLIC = 'Public'
    PRIVATE = 'Private'

class Person(db.Model):
    """Person Model"""
    __tablename__ = 'person'
    idnum = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    title = db.Column(db.String(50), nullable=True)
    location = db.Column(db.String(50), nullable=True)
    dob = db.Column(db.DateTime, nullable=True)
    image_url = db.Column(db.String(512), nullable=True)
    website = db.Column(db.String(512), nullable=True)

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

class Company(db.Model):
    """Company Model"""
    __tablename__ = 'company'
    idnum = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    location = db.Column(db.String(50), nullable=True)
    ownership_type = db.Column(db.Enum(Ownership), nullable=True)
    funding = db.Column(db.Integer, nullable=True)
    description = db.Column(db.String(350), nullable=True)
    ceo_id = db.Column(db.Integer, ForeignKey('person.id'), nullable=True)
    image_url = db.Column(db.String(512), nullable=True)
    size = db.Column(db.Integer, nullable=True)
    website = db.Column(db.String(512), nullable=True)

    def __init__(self, name, location, ownership_type, funding, description,
                 ceo_id, image_url, size, website):
        """Initializes Company, ceo as foreign key and ownership as enum"""
	self.name = name
        self.title = title
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
