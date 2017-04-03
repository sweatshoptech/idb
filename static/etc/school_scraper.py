import requests
import json
import school_config
import models

def fill_school(school):
    school_name = school.name
    if school.idnum <= 3:
        return
    try:
        schoolreq = requests.get("https://api.data.gov/ed/collegescorecard/v1/schools?school.name={0}&api_key={1}".format(school_name, school_config.key))
        data = json.loads(schoolreq.text)
        print(school_name)
        if data["results"]:
            print(data["results"][0]["school"]["city"])
            print(data["results"][0]["school"]["state"])
            print(data["results"][0]["school"]["school_url"])
            print(data["results"][0]["2013"]["student"]["size"])
            school.location = data["results"][0]["school"]["city"] or data["results"][0]["school"]["state"]
            school.website = data["results"][0]["school"]["school_url"]
            school.size = int(data["results"][0]["2013"]["student"]["size"])
    except:
        pass

if __name__ == "__main__":
    all_schools = models.School.query.all()
    for school in all_schools:
       fill_school(school)
    models.db.session.commit()

