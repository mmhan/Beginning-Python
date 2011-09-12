#!usr/bin/python2
'''
Created on Sep 12, 2011

@author: mike
'''

# A simple database

# A dictionary with person names as keys. Each person is represented as another dict with keys
# 'phone' and 'addr'

def getPhonebook():
    people = {
              'Alice': {
                        'phone' : '2341',
                        'addr'  : 'Foo drive 23'
                        },
              'Beth': {
                       'phone'  : '9102',
                       'addr'   : 'Bar street 42'
                       },
              'Cecil':{
                       'phone'  :"3158",
                       'addr'   :"Baz avenue 90"
                       }
    }
    return people

def phonebook():
    
    people = getPhonebook()
    
    #labels for phone and address for printing
    labels = {
              'phone': "phone number",
              'addr' : "address"
              }
    
    name = raw_input("Name : ")
    
    #are we looking for a phone number or address?
    request = raw_input("Phone number (p) or address (a)? ")
    key = request # In case the request is neither p or a
    if request == 'p': key = 'phone'
    if request == 'a': key = 'addr'
    
    #use get to provide default value
    
    person = people.get(name, {})
    label = labels.get(key, key)
    result = person.get(key, 'not available')
    
    #only try to print information if the name is a valid key in our dictionary
    print "%s's %s is %s." % (name, label, result)
    
phonebook() 