import os, pprint

if __name__ == "__main__":
    f = open('beatles-diskography.csv')
    data = f.readlines()
    headers = data[0]
    headers = headers.split(',')
    headers = map(lambda x: x.strip(), headers)
    print headers
    data = data[1:11]
    for row in data:
        row = row.split(',')
        row = map(lambda x: x.strip(), row)
        dict_tuples = zip(headers,row)
        dictionary = {}
        for key,val in dict_tuples:
            dictionary[key] = val
        pprint.pprint(dictionary)
        print
