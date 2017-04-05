import requests
import json
import models

companies = models.Company.query.all()
names = requests.get("http://country.io/names.json")
codes2 = requests.get("http://country.io/iso3.json")
names = json.loads(names.text)
codes2 = json.loads(codes2.text)
codes3 = {v:k for k,v in codes2.items()}
count = 0

for company in companies:
    if company.country and company.country in codes3:
        code2 = codes3[company.country]
        company.country = names[code2]
        print(code2, company.country)
        count += 1
print(count)
models.db.session.commit()

