import re
from csv import reader

input_str = r""

def get_val(in_list, ind):
    if not in_list[ind] or (in_list[ind] != 'NULL' and in_list[ind][0] != "'"):
        return "'"+in_list[ind]+"'"
    else:
        return in_list[ind]

for each_insert in re.split(r'[()]', input_str):
    print(each_insert)
    if len(each_insert) > 1:
        attrs = []
        for line in reader([each_insert], quotechar="'"):
            attrs = line
        if attrs[0] == ' ':
            attrs = attrs[1:]
        out_string = "INSERT INTO COMPANY(NAME, LOCATION, OWNERSHIP_TYPE, FUNDING, DESCRIPTION, CEO_ID, IMAGE_URL, SIZE, WEBSITE, CRUNCH_ID) VALUES({0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9});"
        desc = 19 if len(attrs[19]) < 350 and attrs[19] != 'NULL' else 18 if attrs[18] != 'NULL' else 19 if attrs[19][:349] != 'NULL' else 17
        print(out_string.format(get_val(attrs, 4), get_val(attrs, 23), 'NULL', get_val(attrs, 32), get_val(attrs, desc), 'NULL', get_val(attrs, 14), 'NULL', get_val(attrs,11), get_val(attrs, 0)))


