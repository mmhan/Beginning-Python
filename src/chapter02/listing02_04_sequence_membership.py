# check a users's pin against data

def authenticate():
    user = raw_input('User : ')
    pin = raw_input("Pin : ")
    
    data = [
            ['foo', '1234'],
            ['bar', '5678'],
            ['bla', '6789'],
            ['yada', '9010'],
            ['user', '1111']
            ]
    
    if [user,pin] in data:
        print "Welcome"
    else:
        print "Invalid user"
        

authenticate()