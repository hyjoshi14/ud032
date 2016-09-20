import os, csv, pprint

if __name__ == '__main__':
    f = open('beatles-diskography.csv','r')
    f_csv_dictReader = csv.DictReader(f)
    for data in f_csv_dictReader:
        pprint.pprint(data)
        print
