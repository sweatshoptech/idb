import requests
import json
import models

def items_from_url(url_string):
    return json.loads(requests.get(url_string).text)["data"]["items"]

def properties_map(iterable, f):
    for i in iterable:
        f(i["properties"])

def add_person(prop):
    try:
        new_person = models.Person("{0} {1}".format(prop["first_name"], prop["last_name"]), prop["title"], prop["city_name"] or prop["region_name"], None, prop["profile_image_url"], prop["homepage_url"])
        models.db.session.add(new_person)
    except(Exception):
        pass

def add_organization(prop):
    try:
       if prop["primary_role"] == "company":
            new_org = models.Company(prop["name"][:50], prop["city_name"] or prop["region_name"], None, None, prop["short_description"], None, prop["profile_image_url"], None, prop["homepage_url"])
       elif prop["primary_role"] == "school":
            new_org = model.School(prop["name"][:50], prop["city_name"] or prop["region_name"], prop["short_description"], prop["profile_image_url"], None, prop["homepage_url"])
       else:
            new_org = models.Investor(prop["name"][:50], prop["city_name"] or prop["region_name"], None, prop["short_description"], prop["profile_image_url"], None, prop["homepage_url"])
       models.db.session.add(new_org)
    except(Exception):
        pass


if __name__ == "__main__":
    people_items = items_from_url("https://api.crunchbase.com/v/3/odm-people?user_key=fb1eb389415ec74fd8f8b55f631e334a")
    properties_map(people_items, add_person)
#   models.db.session.commit()
    org_items = items_from_url("https://api.crunchbase.com/v/3/odm-organizations?user_key=fb1eb389415ec74fd8f8b55f631e334a")
    properties_map(org_items, add_organization)
    print(models.School.query.all()) 
    print(models.Investor.query.all()) 
#    models.db.session.commit()
