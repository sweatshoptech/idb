import requests
from bs4 import BeautifulSoup
import models

def find_website(investor):
    lookup_string = investor.name
    r = requests.get("https://www.google.com/search?client=ubuntu&q=" + lookup_string)
    if r.status_code != 200:
        print("STAHP: " + investor.name)
    soup = BeautifulSoup(r.text, "html.parser")
    investor.website = soup.find('cite').text
    print(investor.website)

def get_investors():
    return (investor for investor in models.Investor.query.all())

def find_next_num(num, investors, investor):
    try:
        for i in range(num):
            find_website(investor)
            investor = next(investors)
    except Exception:
        pass
    return investor
