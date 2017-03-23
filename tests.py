from unittest import main, TestCase
import datetime
import models.py

#
# Person Unit Tests
#

def test_Person_model_1(self):
    """Test querying the database by attribute using simple keywords"""

    with idb.test_request_context():
        example1 = Person("Deepak Sekar", "CEO", "SF",
                           datetime.today(), "www.image.com", "SWEatshop1")

        db.session.add(example1)
        db.session.commit()

        person1 = db.session.query(Person).filter_by(name="Deepak Sekar").first()
        self.assertEqual(person1.title, "CEO")
        self.assertEqual(person1.location, "SF")

        db.session.delete(example1)
        db.session.commit()

def test_Person_model_2(self):
    """Test querying the database by attribute using simple keywords"""

    with idb.test_request_context():
        example2 = Person("Alex Salazar", "CEO", "San Mateo",
                           datetime.today(), "www.image.com", "SWEatshop2")

        db.session.add(example1)
        db.session.commit()

        person2 = db.session.query(Person).filter_by(name="Alex Salazar").first()
        self.assertEqual(person2.idnum, "2")
        self.assertEqual(person2.location, "San Mateo")

        db.session.delete(example2)
        db.session.commit()

def test_Person_model_3(self):
    """Test querying the database by attribute using simple keywords"""

    with idb.test_request_context():
        example3 = Person("Dilip Keshu", "CEO", "Princeton",
                           datetime(1962,1,12), "www.image.com", "borngroup.com")

        db.session.add(example1)
        db.session.commit()

        person3 = db.session.query(Person).filter_by(name="Dilip Keshu").first()
        self.assertEqual(person3.image_url, "www.image.com")
        self.assertEqual(person3.website, "borngroup.com")

        db.session.delete(example3)
        db.session.commit()

#
# Company Unit Tests
#

def test_Company_model_1(self):
    """Test querying the database by attribute using simple keywords"""

    with idb.test_request_context():
        example1 = Company("Chowbotics", "SF", PRIVATE, "6300000"
                           "Company", 1, "www.chowbotics.com/image", 400, "www.chowbotics.com")

        db.session.add(example1)
        db.session.commit()

        company1 = db.session.query(Company).filter_by(name="Chowbotics").first()
        self.assertEqual(company1.funding, "6300000")
        self.assertEqual(company1.location, "SF")

        db.session.delete(example1)
        db.session.commit()

def test_Company_model_2(self):
    """Test querying the database by attribute using simple keywords"""

    with idb.test_request_context():
        example2 = Company("Stormpath", "SJ", PRIVATE, "24700000"
                           "Company", 2, "www.stormpath.com/image", 500, "www.stormpath.com")

        db.session.add(example2)
        db.session.commit()

        company2 = db.session.query(Company).filter_by(name="Stormpath").first()
        self.assertEqual(company2.funding, "24700000")
        self.assertEqual(company2.location, "SJ")

        db.session.delete(example1)
        db.session.commit()

def test_Company_model_3(self):
    """Test querying the database by attribute using simple keywords"""

    with idb.test_request_context():
        example3 = Company("BORN", "NY", PRIVATE, "0"
                           "Company", 3, "www.borngroup.com/image", 600, "www.borngroup.com")

        db.session.add(example3)
        db.session.commit()

        company3 = db.session.query(Company).filter_by(name="BORN").first()
        self.assertEqual(company3.funding, "0")
        self.assertEqual(company3.location, "NY")

        db.session.delete(example3)
        db.session.commit()

#
# School Unit Tests
#

def test_School_model_1(self):
    """Test querying the database by attribute using simple keywords"""

    with idb.test_request_context():
        example1 = School("IITM", "Chennai", "IIT Madras", "www.iitm.ac.in/image", 10000, "www.iitm.ac.in")

        db.session.add(example1)
        db.session.commit()

        school1 = db.session.query(School).filter_by(name="IITM").first()
        self.assertEqual(school1.size, 10000)
        self.assertEqual(school1.location, "Chennai")

        db.session.delete(example1)
        db.session.commit()


def test_School_model_2(self):
    """Test querying the database by attribute using simple keywords"""

    with idb.test_request_context():
        example2 = School("GA Tech", "Atlanta", "Georgia Tech", "www.gatech.edu/image", 26806, "www.gatech.edu")

        db.session.add(example2)
        db.session.commit()

        school2= db.session.query(School).filter_by(name="GA Tech").first()
        self.assertEqual(school2.size, 26806)
        self.assertEqual(school2.location, "Atlanta")

        db.session.delete(example2)
        db.session.commit()


def test_School_model_3(self):
    """Test querying the database by attribute using simple keywords"""

    with idb.test_request_context():
        example3 = School("Stanford", "Stanford", "Stanford GSB", "www.gsb.stanford.edu/image", 4000, "www.gsb.stanford.edu")

        db.session.add(example3)
        db.session.commit()

        school3= db.session.query(School).filter_by(name="Stanford").first()
        self.assertEqual(school3.size, 4000)
        self.assertEqual(school3.location, "Stanford")

        db.session.delete(example3)
        db.session.commit()

#
# Investor Unit Tests
#

def test_Investor_model_1(self):
    """Test querying the database by attribute using simple keywords"""

    with idb.test_request_context():
        example1 = Investor("Geekdom Fund", "San Antonio", 100, "High Rollers", "http://geekdomfund.com/image", "http://geekdomfund.com")

        db.session.add(example1)
        db.session.commit()

        investor1 = db.session.query(Investor).filter_by(name="Geekdom Fund").first()
        self.assertEqual(investor1.funding, 100)
        self.assertEqual(investor1.location, "San Antonio")

        db.session.delete(example1)
        db.session.commit()


def test_Investor_model_2(self):
    """Test querying the database by attribute using simple keywords"""

    with idb.test_request_context():
        example2 = Investor("Pelion Venture Partners", "SLC", 100000, "VCs", "http://pelionvp.com/image", "http://pelionvp.com")

        db.session.add(example2)
        db.session.commit()

        investor2 = db.session.query(Investor).filter_by(name="Pelion Venture Partners").first()
        self.assertEqual(investor2.funding, 100000)
        self.assertEqual(investor2.location, "SLC")

        db.session.delete(example2)
        db.session.commit()



def test_Investor_model_3(self):
    """Test querying the database by attribute using simple keywords"""

    with idb.test_request_context():
        example3 = Investor("Scale Venture Partners", "Foster City", 10, "Investors", "http://scalevp.com/image", "http://scalevp.com")

        db.session.add(example3)
        db.session.commit()

        investor3 = db.session.query(Investor).filter_by(name="Scale Venture Partners").first()
        self.assertEqual(investor3.funding, 10)
        self.assertEqual(investor3.location, "Foster City")

        db.session.delete(example3)
        db.session.commit()


#
# Category Unit Tests
#

def test_Category_model_1(self):
    """Test querying the database by attribute using simple keywords"""

    with idb.test_request_context():
        example1 = Category("Social")

        db.session.add(example1)
        db.session.commit()

        category1 = db.session.query(Category).filter_by(name="Social").first()
        self.assertEqual(category1.name, "Social")

        db.session.delete(example1)
        db.session.commit()


def test_Category_model_2(self):
    """Test querying the database by attribute using simple keywords"""

    with idb.test_request_context():
        example1 = Category("Retail")

        db.session.add(example2)
        db.session.commit()

        category2 = db.session.query(Category).filter_by(name="Retail").first()
        self.assertEqual(category2.name, "Retail")

        db.session.delete(example2)
        db.session.commit()


def test_Category_model_3self):
    """Test querying the database by attribute using simple keywords"""

    with idb.test_request_context():
        example1 = Category("Payments")

        db.session.add(example3)
        db.session.commit()

        category3 = db.session.query(Category).filter_by(name="Payments").first()
        self.assertEqual(category3.name, "Payments")

        db.session.delete(example3)
        db.session.commit()