from urllib import urlopen, urlretrieve
import re

def urlOpen():
    '''
    Open a url, return fileobject, searches stuff on it.
    '''
    
    webpage = urlopen('http://www.python.org')
    
    text = webpage.read()
    
    m = re.search('<a href="([^"]+)" .*?>about</a>', text, re.IGNORECASE)
    print m.group(1)

def urlRetrieve():
    '''
    Retrieve a url and then save it as a html
    '''    
    urlretrieve('http://www.python.org', 'C:\\python_webpage.html')
    
urlRetrieve()