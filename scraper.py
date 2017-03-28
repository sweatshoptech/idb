import requests
import json
import models

all_people = json.loads(requests.get("https://api.crunchbase.com/v/3/odm-people?user_key=fb1eb389415ec74fd8f8b55f631e334a").text)
pd = []
for pp in all_people["data"]["items"]:
    p1=pp["properties"]
    try:
        np = models.Person("{0} {1}".format(p1["first_name"], p1["last_name"]), p1["title"], p1["city_name"] or p1["region_name"], p1.get("dob"), p1["profile_image_url"], p1["homepage_url"])
        pd.append(np)
    except(Exception):
        pass
