import requests
from bs4 import BeautifulSoup
import models

def find_website(school):
    lookup_string = school.name
    r = requests.get("https://www.google.com/search?client=ubuntu&q=" + lookup_string)
    if r.status_code != 200:
        print("STAHP: " + school.name)
    soup = BeautifulSoup(r.text, "html.parser")
    school.website = soup.find('cite').text
    print(school.website)
    
def get_schools():
    return (school for school in models.School.query.all())
