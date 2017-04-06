import requests
import models
import json


def find_image(person):
    lookup_string = school.name
    r = requests.get("https://api.cognitive.microsoft.com/bing/v5.0/images/search + lookup_string + )
    if r.status_code != 200:
        print("STAHP: " + person.name)
    data = json.dumps(r.text)
    print(data["link"])
    
def get_people():
    return (person for person in models.Person.query.all() if person.image_url is None)

def find_next_num(num, people, person):
    for i in range(num):
        find_website(person)
        person = next(people)
    return person



