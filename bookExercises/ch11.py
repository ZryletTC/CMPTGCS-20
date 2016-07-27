from urllib2 import urlopen
def getSource(url):
    'returns the source document from a given url'
    response = urlopen(url)
    return response.read()

def news(url, lst):
    'returns the number of time each topic in lst is on the webpage at url'
    html = urlopen(url).read()
    for topic in lst:
        print "{} appears {} times.".format(topic,html.count(topic))

from HTMLParser import HTMLParser
class LinkParser(HTMLParser):
    '''HTML doc parser that prints values of
        href attributes in anchor start tags'''

    def handle_starttag(self, tag, attrs):
        'print value of href attribute if any'

        if tag == 'a':
            for attr in attrs:
                if attr[0] == 'href':
                    print attr[1]
                
class MyHTMLParser(HTMLParser):
    global indent

    def __init__(self):
        HTMLParser.__init__(self)
        self.indent = 0
        
    def handle_starttag(self, tag, attrs):
        print "\t"*self.indent+tag+" start"
        self.indent += 1

    def handle_endtag(self, tag):
        print "\t"*self.indent+tag+" end"
        self.indent -= 1

from urlparse import urljoin
class Collector(HTMLParser):
    'collects hyperlink URLs into a list'

    def __init__(self,url):
        HTMLParser.__init__(self)
        self.url = url
        self.links = []
        self.data = ""

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for attr in attrs:
                if attr[0] == 'href':
                    absolute = urljoin(self.url, attr[1])
                    if absolute[:4] == 'http':
                        self.links.append(absolute)

    def handle_data(self, data):
        self.data += data


    def getLinks(self):
        return self.links

    def getData(self):
        return self.data

from re import findall
def frequency(string):
    words = findall('[a-zA-Z]+',string)
    res = {}
    for word in words:
        res[word] = string.count(word)
    return res
