#!/usr/bin/python2

'''
Created on Sep 12, 2011

@author: mike
'''

def dictionaries():
    phonebook = {'Alice': '2341', 'Beth': '9102', 'Cecil': "3258"}  #straightforward declaration
    print phonebook
    
    items= [('name', 'Gumby'), ('age', 42)]
    
    d = dict(items)                                                 #declare using list of tuples (name, value)
    print d   
    
    d = dict(name = 'Gumby', age = 42)                              #declare using arguments
    print d
    
    print d['name']                         #access info at key
    
    '''Formatting string output using dictionary'''
    print "Cecil's phone number is %(Cecil)s." % phonebook
    
    '''Dict methods'''
    
    #to copy
    from copy import deepcopy
    x = {}
    x['names'] = ['Alfred', 'Bertrand']
    c = x.copy()        #create shallow copy of d as x
    dc = deepcopy(x)    #deep copy
    
    x['names'].append('Clive')
    print c
    print dc
    
        
    print d
    d.clear()       #clear the dict, useful for clearing copy of d as well, in case of e = d before clear(). because d = {} won't clear e.
    print d
    
    #fromkeys() create dict from keys using default value if given
    print {}.fromkeys(("name", "addr"))
    print {}.fromkeys(("name", "addr"), "Unknown")
    
    #get() forgiving way of accessing data from dict, no exception thrown
    print d.get("bla")
    print d.get("bla", "Nothing")
    
    #has_key() checks for existence of key, same as: key in dict
    print d.has_key("bla")
    
    #items() and iteritems() returns list of tuples of items or iterator of items.
    print x.items()
    print x.iteritems()
    
    #keys() and iterkeys() returns list of keys or iterator of keys
    print x.keys()
    print x.iterkeys()
    
    #pop() - pops out given key
    print x.pop('names')
    
    #popitem() - pops random item from dict in tuple
    d = {'url': "http://www.python.org", 'spam' : False,'title' : 'Python Web Site'}
    print d.popitem()
    
    #setdefault() - is similar to 'get': will set something as default val and return that value if no value exist, if value exist will return value.
    print d.setdefault('url', 'Unknown')
    print d.setdefault('bookmarked', False)
    print d
    
    #update() - will update a dict with another dict (kinda like merge)
    d.update({'url' : 'http://www.python.org/?updated'})
    print d
    
    #values() and itervalues() - return list of values of iterator of values.
    print d.values()
    print d.itervalues()
    
    
    
dictionaries()