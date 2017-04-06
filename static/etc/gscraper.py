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
    school.size = 1
    print(school.website)
    
def get_schools():
    return (school for school in models.Company.query.all() if school.website is None)

def find_next_num(num, schools, school):
    for i in range(num):
        find_website(school)
        school = next(schools)
    return school

