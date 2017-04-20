select * from investor;

INSERT INTO INVESTOR(NAME)
SELECT distinct CBO.investor_object_id
FROM cb_investments AS CBO JOIN COMPANY AS C ON CBO.funded_object_id = C.CRUNCH_ID
where investor_object_id is not null;

INSERT INTO INVESTMENT(INVESTOR_ID, COMPANY_ID)
SELECT I.IDNUM, C.IDNUM
FROM cb_investments AS CBO JOIN INVESTOR AS I ON CBO.investor_object_id = I.NAME 
JOIN COMPANY AS C ON CBO.funded_object_id = C.CRUNCH_ID;


select count(*) from investor;
