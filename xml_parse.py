import os, pprint
from bs4 import BeautifulSoup as bs

## Solution to Quiz:Extracting Data
def main_bs():
    print os.getcwd()
    f_xml = open('exampleResearchArticle.xml','r')
    soup = bs(f_xml.read(),'lxml')
    authors = soup.findAll('au')
    out = []
    for author in authors:
        author_dict = {}
        for child in author.childGenerator():
            if child == u'\n' or 'insr' == child.name:
                    continue
            else:
                print child.name,':', child.get_text().strip()
                author_dict[child.name] = child.get_text().strip()
        pprint.pprint(author_dict)
        print
        out.append(author_dict)
    return out

## Solution to Quiz:Handling Attributes
def main_bs2():
    print os.getcwd()
    f_xml = open('exampleResearchArticle.xml','r')
    soup = bs(f_xml.read(),'lxml')
    authors = soup.findAll('au')
    out = []
    for author in authors:
        author_dict = {'insr':[]}
        for child in author.childGenerator():
            if child == u'\n':
                    continue
            elif child.name == 'insr':
                author_dict['insr'] += [child['iid'].strip()]
            else:
                print child.name,':', child.get_text().strip()
                author_dict[child.name] = child.get_text().strip()
        pprint.pprint(author_dict)
        print
        out.append(author_dict)
    return out

if __name__ == '__main__':
    pprint.pprint(main_bs())
    pprint.pprint(main_bs2())
