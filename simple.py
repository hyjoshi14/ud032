import os, pprint

if __name__ == "__main__":
    f = open('beatles-diskography.csv')
    data = f.readlines()
    headers = data[0]
    headers = headers.split(',')
    headers = map(lambda x: x.strip(), headers)
    print headers
    data = data[1:]
    for i in range(len(data)):
            row = data[i]
            row = row.split(',')
            if len(row) != len(headers):
                print 'Row %d is causing a problem' %(i+1)
                continue
            row = map(lambda x: x.strip(), row)
            dict_tuples = zip(headers,row)
            dictionary = {}
            for key,val in dict_tuples:
                dictionary[key] = val
            pprint.pprint(dictionary)
            print
