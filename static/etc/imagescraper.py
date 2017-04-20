import requests
import models
import json
import httplib, urllib, base64




headers = {
    # Request headers
    'Ocp-Apim-Subscription-Key': '',
}



def find_image(person):
    try:
        lookup_string = person.name
        params = urllib.urlencode({
        # Request parameters
        'q': lookup_string,
        'count': '1',
        'offset': '0',
        })
        conn = httplib.HTTPSConnection('api.cognitive.microsoft.com')
        conn.request("GET", "/bing/v5.0/images/search?%s" % params, "{body}", headers)
        response = conn.getresponse()
        requesttext = response.read()
        data = json.loads(requesttext)
        person.image_url = data["value"][0]["thumbnailUrl"]
        print(person.image_url)
        conn.close()
    except Exception as e:
        pass
    

def get_people():
    return (person for person in models.Person.query.all() if person.image_url is None)

def find_next_num(num, people, person):
    count = 0
    for i in range(num):
        count += 1
        find_image(person)
        if count % 10 == 0:
            models.db.session.commit()
        person = next(people)
    models.db.session.commit()
    return person



