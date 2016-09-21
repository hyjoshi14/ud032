import os, pprint
from bs4 import BeautifulSoup as bs

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

if __name__ == '__main__':
    pprint.pprint(main_bs())
