#!usr/bin/python2
'''
Created on Sep 12, 2011

@author: mike
'''

def printImport():
    
    print "Age", 42 # you can print with comma, will translate into space
    
    print "Age",    # end with comma to prevent line break
    print 42
    
    print 1,2,3     # will get space in between numbers
    
    import math as maa
    from math import sqrt as squareRoot
    
    print maa.sqrt(9)
    print squareRoot(9)
    
    
def assignmentMagic():
    a,b,c = 1,2,3   # sequence unpacking a becomes 1, b-2, c-3
    print a,b,c
    
    x, y = 1,2
    x, y = y, x     #useful in interchanging variables
    
    print x,y
    
    scoundrel = {'name': 'Robin', 'girlfriend' : 'Marion'}
    key, value = scoundrel.popitem()        #useful in this case too.
    
    print key, value
    
    '''chained assignments'''
    x = y = printImport()       # will have none, but you get the drift
    # above is equal to 
    x = printImport()
    y = x
    # but in other functions might not be equal to 
    x = printImport()           # the result may not be same if it's return current time or something.
    y = printImport()
    
def ifelseBlocks():
    num = input("Enter a number : ")
    if num > 0:
        print "The number is positive"
    elif num == 0:
        print "The number is zero"
    else:
        print "The number is negative"
    
def nestingBlocks():
    name = raw_input("What is your name?")
    if name.endswith('Gumby'):
        if name.startswith("Mr."):
            print 'Hello, Mr. Gumby'
        else:
            print 'Hello, Ms. Gumby'
    else:
        print 'Hello, Stranger'
        
def otherOperators():
    '''
    This is example of all other comparing operators
    '''
    print "foo" == 'bar' #make sure it's not =
    
    x = y = [1,2,3]
    z = [1,2,3]
    
    assert x == y, "X and Y must be same"        #expect true
    
    assert x == z, "X and Z must be same using this operator too.. since they both contain same elements"
    
    assert x is y, 'Y is pointing to same mem loc as X'
    
    assert x is not z, 'But Z isn\'t'
    
    '''
    To illustrate the point above
    '''
    x = [1,2,3]
    y = [2,4]
    assert x is not y, "Obvious, ain't it?"
    assert x != y, "This too is obvious"
    
    del x[2]
    y[1] = 1
    y.reverse()
    
    assert x == y, "Now it'll contain same stuff"
    assert x is not y, "but they are still diff lists"
    
    '''
    in: the membership operator
    '''
    name = raw_input("What is your name? ")
    if 's' in name:
        print "Your name contains letter 's'."
    else: 
        print "Your name doesn't contain letter 's'"
        
    '''
    comparing strings
    '''
    assert 'alpha' < 'beta', "Use alphabetical order"
    
    assert 'FnOrD'.lower() == 'Fnord'.lower(),  "Use lower() to make sure that the comparison is case-insensitive"
    
    assert [1,2] < [3,4], 'This uses the elements in the list to compare between lists'
    
    assert [2,[3,4]] > [2,[1,5]], 'It can go in more.'
    
    '''
    Text talk about boolean operators and, or
    and then assertion as shown above
    '''
    
def loops():
    '''
    In this function we'll look into how loops are created.
    '''
    
    ### While loops
    name = ''
    while not name.strip():
        name = raw_input('What is your name? ')
    print "Hi", name
    
    ### For loops
    sentence = "A quick brown fox jumps over the lazy dog"
    for word in sentence.split(): #sentence.split() create a list (or tuple) of words (splitted by white space)
        print word
    
    #tips:: use them in for loops
    range(100)  # will result as a list of [0,99]
    range(1,101) # will result as 1-100
    
    ### iterating over dictionaries
    d = dict(zip(('a','b','c'), (1,2,3)))   # zip() will map a => 1, b => 2, c => 3 into (a,1), (b,2), (c,3) sequence
    for key in d:
        print key, 'corresponds to ', d[key]
        
    for key, val in d.items():              # will bring it back to zip() stage
        print key, 'corresponds to ', val
    
    ### numbered iterations
    strings = ['bla', 'yada', 'xxx', 'nada']
    for index, string in enumerate(strings):
        if 'xxx' in string:
            strings[index] = '[censored]'
    print strings
    
    ## sorted() returns sorted list
    ## reversed() returns reversed iterator
    
    from math import sqrt
    for n in range(99,0, -1):
        root = sqrt(n)
        if root == int(root):
            print n
            break
    ## there is also continue

def whileTrueBreak():
    ## while True/break idiom
    while True:
        word = raw_input("Please enter your name: ")
        if not word: break
        
        # do something with word
        print "The word was", word

def breakElse():
    '''
    Attach else at the end of for loop to execute when the loop didn't get a break
    '''
    from math import sqrt
    for n in range(99,81, -1):
        root = sqrt(n)
        if root == int(root):
            print n
            break
    else:
        print "Didn't find it"
        
def listComprehension():
    '''
    Creating lists using loops
    '''
    print [x*x for x in range(10)]
    
    print [x*x for x in range(10) if x % 3 == 0]
    
    print [(x,y) for x in range(3) for y in range(3)]
    # combining with if
    girls = ['alice', 'bernice', 'clarice']
    boys  = ['chris', 'arnold', 'bob']

    print [b + '+' + g for b in boys for g in girls if b[0] == g[0]]    
    print [b + '+' + g for g in girls for b in boys if b[0] == g[0]]    # to take note of the order of the two results
    
def betterBGSolution():
    '''
    Better boy and girl matching solution in the tips
    this doesn't check all possibilities
    '''
    girls = ['alice', 'bernice', 'clarice']
    boys  = ['chris', 'arnold', 'bob']
    
    letterGirls = {}
    for girl in girls:
        letterGirls.setdefault(girl[0], []).append(girl)
    
    print [b + '+' + g for b in boys for g in letterGirls[b[0]]]
    
def execEval():
    # pass is a placeholder for expressions
    # del delete the variable
    # exec or eval is used to execute things from string, 
    # you could provide scope to exec or eval
    
    #    exec 'bla = 1'
    #    print bla
    
    #    scope = {}
    #    exec 'bla = 1' in scope
    #    print scope['bla']
    pass

execEval()