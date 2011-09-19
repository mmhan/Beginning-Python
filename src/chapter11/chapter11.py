#!usr/bin/python2

def simpleOpen():
    '''
    Doing some simple file open tasks
    '''
    #f = open(r'C:\text\somefile.txt')
    
    f = open(r'somefile.txt')
    
def simpleWrite():
    '''
    Doing simple file write task
    '''
    f = open(r'somefile.txt', 'w')
    f.write('Hello, ')
    f.write('World!')
    f.close()
    
def simpleRead():
    '''
    Doing simple file reading task
    '''
    f = open(r'somefile.txt', 'r')
    print f.read(4) #Hell
    print f.read()  #o, World!
    
def randomAccess():
    '''
    Doing seek()s 
    '''
    f = open(r'randomaccess.txt', 'w')
    f.write("012345678910234567890012345678901234567890123456789")
    f.seek(5)
    f.write("Hello, world")
    f.close()
    
    f = open(r'randomaccess.txt', 'r')
    print f.read()
    f.close()
    
    f = open(r'randomaccess.txt', 'r')
    f.read(2)
    f.read(5)
    print f.tell()
    

def closingFiles():
    '''
    Closing file should be in finally: 
    '''
    # like this
    try:
        #write data to your file
        pass
    finally:
        #file.close()
        pass
    
    #from py 2.5 onwards
    with open("randomaccess.txt") as somefile:
        #do_something(somefile)
        pass
        #the file is automatically closed as soon as this block is exited.
    
closingFiles()