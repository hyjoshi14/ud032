import os, csv, pprint,re

autos_csv = open('autos.csv','r')
autos_dict_reader = csv.DictReader(autos_csv)
print autos_dict_reader.fieldnames
good_output = []
bad_output = []

year_re = re.compile(r'^\d{4}')
def extract_year(row):
    year_field_value = row['productionStartYear']
    year_match_obj = year_re.search(year_field_value)
    return year_match_obj

def validity():
    for row in autos_dict_reader:
        if 'dbpedia' not in row['URI']:
            continue
        else:
            year_match_obj = extract_year(row)
            if not year_match_obj:
                bad_output.append(row)
            else:
                year = year_match_obj.group()
                if int(year) >=1886 and int(year) <= 2014:
                    row['productionStartYear'] = year
                    good_output.append(row)
                else:
                    bad_output.append(row)

if __name__ == '__main__':
    validity()
    pprint.pprint(good_output)
    pprint.pprint(bad_output)
    print len(good_output)
    print len(bad_output)
