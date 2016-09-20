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
        try:
            print 'Trying row %d' %(i+1)
            row = data[i]
            row = row.split(',')
            row = map(lambda x: x.strip(), row)
            dict_tuples = zip(headers,row)
            dictionary = {}
            for key,val in dict_tuples:
                dictionary[key] = val
            pprint.pprint(dictionary)
            print
        except:
            print 'Row %d is showing an error' %(i+1)
