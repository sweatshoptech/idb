import requests
import json

school_name = "Georgia Institute of Technology"
school = requests.get("https://api.data.gov/ed/collegescorecard/v1/schools?school.name={0}&api_key={1}".format(school_name, key))
data = json.loads(school.text)
print(data["results"][0]["school"]["city"])
print(data["results"][0]["school"]["state"])
print(data["results"][0]["school"]["school_url"])
print(data["results"][0]["2013"]["student"]["size"])
