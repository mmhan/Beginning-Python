from urllib import urlopen
from HTMLParser import HTMLParser

class Scraper(HTMLParser):
    '''
    This won't work due to structural change from python.org
    '''
    in_h3 = False
    in_link = False
    
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'h3':
            self.in_h3 = True
            
        if tag == 'a' and 'href' in attrs:
            self.in_link = True
            self.chunks = []
            self.url = attrs['href']
            
    def handle_data(self, data):
        if self.in_link:
            self.chunks.append(data)
            
    def handle_endtag(self, tag):
        if tag == 'h3':
            self.in_h3 = False
        if tag == 'a':
            if self.in_h3 and self.in_link:
                print "%s (%s)" % (''.join(self.chunks), self.url)
            self.in_link =  False
            
def scrape(url):
    text = urlopen(url).read()
    parser = Scraper()
    parser.feed(text)
    parser.close()
    
scrape('http://python.org/community/jobs')