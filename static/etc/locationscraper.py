import requests
import models
import json
from bingmaps.apiservices import LocationByQuery

key = ''

def find_country(investor):
    try:
        lookup_string = investor.location
        data = {'q': lookup_string, 
        'key': key}
        response = LocationByQuery(data).get_address
        investor.country = response[0]["countryRegion"]
        print(investor.country)
    except:
        pass

def get_investors():
    return (investor for investor in models.Investor.query.all() if investor.country is None)

def find_next_num(num, investors, investor):
    count = 0
    for i in range(num):
        count += 1
        find_country(investor)
        if count % 50 == 0:
            models.db.session.commit()
        investor = next(investors)
    models.db.session.commit()
    return investor



