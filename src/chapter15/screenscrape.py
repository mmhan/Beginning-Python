from urllib import urlopen
import re

def scrapeJobs():
    '''
    This program no longer works due to changes to python.org's job board structure
    use beautifulsoup for html parsing of bad html code.
    '''
    
    p = re.compile('<h2><a .*?> href="(.*?)">(.*?)</a>')
    text = urlopen('http://www.python.org/community/jobs').read()
    print text    
    for url, name in p.findall(text):
        print '%s (%s)' % (name, url)
        
scrapeJobs()