UPDATE PERSON
SET NAME = CB_PEOPLE.FIRST_NAME || ' ' || CB_PEOPLE.LAST_NAME,
LOCATION = CB_PEOPLE.BIRTHPLACE
FROM CB_PEOPLE
WHERE CB_PEOPLE.object_id = PERSON.crunch_id;

select * from person;
