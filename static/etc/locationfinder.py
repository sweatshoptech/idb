import models
import requests
import json

all_schools = models.Company.query.all()
count = 0
for school in all_schools:
    if school.country is not None:
        continue;
    count += 1
    if not school.website:
        continue;
    try:
        entry = requests.get("http://ip-api.com/json/{0}".format(school.website))
        data = json.loads(entry.text)
        if "country" not in data:
            print(school.name, school.website, data)
            school.location = 'San Francisco, USA'
            school.country = 'USA'
            continue;
        school.country = data["country"]
#        if not school.location:
        school.location = "{0}, {1}".format(data["city"], data["country"]) if data["city"] else data["region"] or data["country"] or school.name 
        print(school.country, school.location)
    except Exception:
        print(school.idnum, school.website)
    if count > 140:
        wait = input()
        count = 0
        models.db.session.commit()
models.db.session.commit()
