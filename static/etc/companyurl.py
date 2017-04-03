import models
from urlparse import urlparse

all_comp = models.School.query.all()
for comp in all_comp:
    old = comp.website
    if "http" not in comp.website:
         old = r"http://" + comp.website
    if old is not None and "facebook." not in old and  "wikipedia." not in old and "linkedin." not in old:
        o = urlparse(old)
        comp.website = o.netloc
    print(comp.website)
models.db.session.commit()

