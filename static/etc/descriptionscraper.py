from bs4 import BeautifulSoup
import urllib
import models
import eventlet

eventlet.monkey_patch()

def get_description(entity):
    if entity.description is None:
        try:
            with eventlet.Timeout(10, Exception):
                page = urllib.urlopen("http://{0}".format(entity.website)).read()
                soup = BeautifulSoup(page, "html.parser")
                desc = soup.findAll(attrs={"name":"description"}) 
                entity.description = desc[0]['content'].encode('utf-8')
        except Exception:
            pass
        print(entity.description)

for school in models.Company.query.all():
    get_description(school)
models.db.session.commit()
