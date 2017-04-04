#!/usr/bin/env python -W ignore::ExtDeprecationWarning
from __future__ import print_function
from unittest import main, TestCase
import unittest
from datetime import date
import models
from models import db
import flask
import sys


# depends on flask, flask_sqlalchemy, flask_table, psycopg2
# to run coverage:
# coverage-3.5 run tests.py
# coverage-3.5 report -m --include="models.py","config.py"

    ################   IMPORTANT   ################
    # Because we auto-increment when adding       #
    # categories, the category tests failed with  #
    #                                             #
    # DETAIL:  Key (idnum)=(1) already exists.    #
    # [SQL: 'INSERT INTO category (name) VALUES   #
    # (%(name)s) RETURNING category.idnum']       #
    # [parameters: {'name': 'test_category_1'}]   #
    #                                             #
    # until the tests were run 8 times, and the   #
    # final "Key (idnum)=(20)" error was thrown.  #
    # Then all the category tests started passing #
    # since the autoincremented id became more    #
    # than the 20 categories we have currently in #
    # the database. If more categories are added, #
    # the category tests may begin failing again. #
    ###############################################

#
# Person Unit Tests
#

class TestModels (TestCase):
 

    def test_Person_model_1(self):
        """Test querying the database by attribute using simple keywords"""
    
        with models.APP.test_request_context():
            example1 = models.Person("test_person_1", "CEO", "SF",
                               date.today(), "www.image.com", "SWEatshop1")
            db.session.add(example1)
            db.session.commit()

            person1 = db.session.query(models.Person).filter_by(name="test_person_1").first()
            self.assertEqual(person1.title, "CEO")
            self.assertEqual(person1.location, "SF")
    
            db.session.delete(example1)
            db.session.commit()
    
    def test_Person_model_2(self):
        """Test querying the database by attribute using simple keywords"""
    
        with models.APP.test_request_context():
            example2 = models.Person("test_person_2", "CEO", "San Mateo",
                               date.today(), "www.image.com", "SWEatshop2")
    
            db.session.add(example2)
            db.session.commit()
    
            person2 = db.session.query(models.Person).filter_by(name="test_person_2").first()
            self.assertEqual(person2.dob.date(), date.today())
            self.assertEqual(person2.location, "San Mateo")
    
            db.session.delete(example2)
            db.session.commit()
            
    
    def test_Person_model_3(self):
        """Test querying the database by attribute using simple keywords"""
    
        with models.APP.test_request_context():
            example3 = models.Person("test_person_3", "CEO", "Princeton",
                               date(1962,1,12), "www.image.com", "borngroup.com")
    
            db.session.add(example3)
            db.session.commit()
            
    
            person3 = db.session.query(models.Person).filter_by(name="test_person_3").first()
            self.assertEqual(person3.image_url, "www.image.com")
            self.assertEqual(person3.website, "borngroup.com")
    
            db.session.delete(example3)
            db.session.commit()

    def test_Person_methods(self):
        """"Test __repr__ and get_all_rows"""

        with models.APP.test_request_context():
            example4 = models.Person("test_person_4", "CFO", "UT Austin",
                               date(2017,4,1), "www.google.com", "fakeswe.me")
            initial_len = len(models.Person.get_all_rows())

            db.session.add(example4)
            db.session.commit()

            changed_len = len(models.Person.get_all_rows())
            person4 = db.session.query(models.Person).filter_by(name="test_person_4").first()

            self.assertEqual(initial_len + 1, changed_len)
            self.assertEqual(repr(person4), "<Person test_person_4>")

            db.session.delete(example4)
            db.session.commit()
            self.assertEqual(len(models.Person.get_all_rows()), initial_len)
    
    #
    # Company Unit Tests
    #
    
    def test_Company_model_1(self):
        """Test querying the database by attribute using simple keywords"""
    
        with models.APP.test_request_context():
            example1 = models.Company("test_company_1", "SF", None, 6300000,
                               "Company", 1, "www.chowbotics.com/image", 400, "www.chowbotics.com")
    
            db.session.add(example1)
            db.session.commit()
            
    
            company1 = db.session.query(models.Company).filter_by(name="test_company_1").first()
            self.assertEqual(company1.funding, 6300000)
            self.assertEqual(company1.location, "SF")
    
            db.session.delete(example1)
            db.session.commit()
            
    
    def test_Company_model_2(self):
        """Test querying the database by attribute using simple keywords"""
    
        with models.APP.test_request_context():
            example2 = models.Company("test_company_2", "SJ", None, 24700000,
                               "Company", 2, "www.stormpath.com/image", 500, "www.stormpath.com")
    
            db.session.add(example2)
            db.session.commit()
            
    
            company2 = db.session.query(models.Company).filter_by(name="test_company_2").first()
            self.assertEqual(company2.funding, 24700000)
            self.assertEqual(company2.location, "SJ")
    
            db.session.delete(example2)
            db.session.commit()
            
    
    def test_Company_model_3(self):
        """Test querying the database by attribute using simple keywords"""
    
        with models.APP.test_request_context():
            example3 = models.Company("test_company_3", "NY", None, 0,
                               "Company", 3, "www.borngroup.com/image", 600, "www.borngroup.com")
    
            db.session.add(example3)
            db.session.commit()
            
    
            company3 = db.session.query(models.Company).filter_by(name="test_company_3").first()
            self.assertEqual(company3.funding, 0)
            self.assertEqual(company3.location, "NY")
    
            db.session.delete(example3)
            db.session.commit()
            
    def test_Company_methods(self):
        """"Test __repr__ and get_all_rows"""

        with models.APP.test_request_context():
            example4 = models.Company("test_company_4", "TX", None, 350,
                               "sweatshop", None, "realimage.png", 350, "sweatshop.org")
            initial_len = len(models.Company.get_all_rows())

            db.session.add(example4)
            db.session.commit()

            changed_len = len(models.Company.get_all_rows())
            company4 = db.session.query(models.Company).filter_by(name="test_company_4").first()

            self.assertEqual(initial_len + 1, changed_len)
            self.assertEqual(repr(company4), "<Company test_company_4>")

            db.session.delete(example4)
            db.session.commit()
            self.assertEqual(len(models.Company.get_all_rows()), initial_len)
 
    
    #
    # School Unit Tests
    #
    
    def test_School_model_1(self):
        """Test querying the database by attribute using simple keywords"""
    
        with models.APP.test_request_context():
            example1 = models.School("test_school_1", "Chennai", "IIT Madras", "www.iitm.ac.in/image", 10000, "www.iitm.ac.in")
    
            db.session.add(example1)
            db.session.commit()
            
    
            school1 = db.session.query(models.School).filter_by(name="test_school_1").first()
            self.assertEqual(school1.size, 10000)
            self.assertEqual(school1.location, "Chennai")
    
            db.session.delete(example1)
            db.session.commit()
            
    
    
    def test_School_model_2(self):
        """Test querying the database by attribute using simple keywords"""
    
        with models.APP.test_request_context():
            example2 = models.School("test_school_2", "Atlanta", "Georgia Tech", "www.gatech.edu/image", 26806, "www.gatech.edu")
    
            db.session.add(example2)
            db.session.commit()
            
    
            school2= db.session.query(models.School).filter_by(name="test_school_2").first()
            self.assertEqual(school2.size, 26806)
            self.assertEqual(school2.location, "Atlanta")
    
            db.session.delete(example2)
            db.session.commit()
            
    
    
    def test_School_model_3(self):
        """Test querying the database by attribute using simple keywords"""
    
        with models.APP.test_request_context():
            example3 = models.School("test_school_3", "Stanford", "Stanford GSB", "www.gsb.stanford.edu/image", 4000, "www.gsb.stanford.edu")
    
            db.session.add(example3)
            db.session.commit()
            
    
            school3= db.session.query(models.School).filter_by(name="test_school_3").first()
            self.assertEqual(school3.size, 4000)
            self.assertEqual(school3.location, "Stanford")
    
            db.session.delete(example3)
            db.session.commit()

            
    def test_School_methods(self):
        """"Test __repr__ and get_all_rows"""

        with models.APP.test_request_context():
            example4 = models.School("test_school_4", "2kewl4skewl", "2kewl", "www2.kewl4.skewl/bro.png",
                               420, "www2.kewl4.skewl")
            initial_len = len(models.School.get_all_rows())

            db.session.add(example4)
            db.session.commit()

            changed_len = len(models.School.get_all_rows())
            school4 = db.session.query(models.School).filter_by(name="test_school_4").first()

            self.assertEqual(initial_len + 1, changed_len)
            self.assertEqual(repr(school4), "<School test_school_4>")

            db.session.delete(example4)
            db.session.commit()
            self.assertEqual(len(models.School.get_all_rows()), initial_len)
 
   
    #
    # Investor Unit Tests
    #
    
    def test_Investor_model_1(self):
        """Test querying the database by attribute using simple keywords"""
    
        with models.APP.test_request_context():
            example1 = models.Investor("test_investor_1", "San Antonio", 100, "High Rollers", "http://geekdomfund.com/image", "http://geekdomfund.com")
    
            db.session.add(example1)
            db.session.commit()
            
    
            investor1 = db.session.query(models.Investor).filter_by(name="test_investor_1").first()
            self.assertEqual(investor1.funding, 100)
            self.assertEqual(investor1.location, "San Antonio")
    
            db.session.delete(example1)
            db.session.commit()
            
    
    
    def test_Investor_model_2(self):
        """Test querying the database by attribute using simple keywords"""
    
        with models.APP.test_request_context():
            example2 = models.Investor("test_investor_2", "SLC", 100000, "VCs", "http://pelionvp.com/image", "http://pelionvp.com")
    
            db.session.add(example2)
            db.session.commit()
            
    
            investor2 = db.session.query(models.Investor).filter_by(name="test_investor_2").first()
            self.assertEqual(investor2.funding, 100000)
            self.assertEqual(investor2.location, "SLC")
    
            db.session.delete(example2)
            db.session.commit()
            
    
    
    
    def test_Investor_model_3(self):
        """Test querying the database by attribute using simple keywords"""
    
        with models.APP.test_request_context():
            example3 = models.Investor("test_investor_3", "Foster City", 10, "Investors", "http://scalevp.com/image", "http://scalevp.com")
    
            db.session.add(example3)
            db.session.commit()
            
    
            investor3 = db.session.query(models.Investor).filter_by(name="test_investor_3").first()
            self.assertEqual(investor3.funding, 10)
            self.assertEqual(investor3.location, "Foster City")
    
            db.session.delete(example3)
            db.session.commit()

            
    def test_Investor_methods(self):
        """"Test __repr__ and get_all_rows"""

        with models.APP.test_request_context():
            example4 = models.Investor("test_investor_4", "Kewlville", 350, "Kewl investors", "kewlinvestors.org/moi.png", "kewlinvestors.org")
            initial_len = len(models.Investor.get_all_rows())

            db.session.add(example4)
            db.session.commit()

            changed_len = len(models.Investor.get_all_rows())
            investor4 = db.session.query(models.Investor).filter_by(name="test_investor_4").first()

            self.assertEqual(initial_len + 1, changed_len)
            self.assertEqual(repr(investor4), "<Investor test_investor_4>")

            db.session.delete(example4)
            db.session.commit()
            self.assertEqual(len(models.Investor.get_all_rows()), initial_len)
    
    
    #
    # Category Unit Tests
    #
    
    def test_Category_model_1(self):
        """Test querying the database by attribute using simple keywords"""
    
        with models.APP.test_request_context():
            example1 = models.Category("test_category_1")
    
            db.session.add(example1)
            db.session.commit()
            
    
            category1 = db.session.query(models.Category).filter_by(name="test_category_1").first()
            self.assertEqual(category1.name, "test_category_1")
    
            db.session.delete(example1)
            db.session.commit()
            
    
    
    def test_Category_model_2(self):
        """Test querying the database by attribute using simple keywords"""
    
        with models.APP.test_request_context():
            example2 = models.Category("test_category_2")
    
            db.session.add(example2)
            db.session.commit()
            
    
            category2 = db.session.query(models.Category).filter_by(name="test_category_2").first()
            self.assertEqual(category2.name, "test_category_2")
    
            db.session.delete(example2)
            db.session.commit()
            
    
    
    def test_Category_model_3(self):
        """Test querying the database by attribute using simple keywords"""
    
        with models.APP.test_request_context():
            example3 = models.Category("test_category_3")
    
            db.session.add(example3)
            db.session.commit()
            
    
            category3 = db.session.query(models.Category).filter_by(name="test_category_3").first()
            self.assertEqual(category3.name, "test_category_3")
    
            db.session.delete(example3)
            db.session.commit()
            
    def test_Category_methods(self):
        """"Test __repr__ and get_all_rows"""

        with models.APP.test_request_context():
            example4 = models.Category("test_category_4")
            initial_len = len(models.Category.get_all_rows())

            db.session.add(example4)
            db.session.commit()

            changed_len = len(models.Category.get_all_rows())
            category4 = db.session.query(models.Category).filter_by(name="test_category_4").first()

            self.assertEqual(initial_len + 1, changed_len)
            self.assertEqual(repr(category4), "<Category test_category_4>")

            db.session.delete(example4)
            db.session.commit()
            self.assertEqual(len(models.Category.get_all_rows()), initial_len)


# ----
# main
# ----

if __name__ == "__main__":  # pragma: no cover
    main()

