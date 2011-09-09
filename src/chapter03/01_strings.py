# for strings

# - Strings are immutable, can't do str[3:0] = 'haha'



def strFormatShort():
    '''
    Formatting strings
    '''
    
    print "Hello %s, %s enough for you?" % ("World", "hot");
    
    ## Formatting floating points
    from math import pi
    print 'PI with three decimals %.3f' % pi
    
strFormatShort()

def strTemplate():
    '''
    Using template
    '''
    from string import Template
    s = Template("$x is really ${x}-ly") #if one is using $ go with $$
    print s.substitute(x='Bla')
    
    s2 = Template("$subj is ${adj}!")
    d = {}
    d['subj'] = "Chocolate"
    d['adj'] = 'awesome'
    print s2.substitute(d)
    
def simpleConversion():
    '''
    Doing simple conversions on string
    '''
    print 'Price of eggs: $%d' % 42
    
    print 'Hex price of eggs: %x' % 42
    
    from math import pi
    print 'Pi : %f...' % pi
    
    print 'Very inexact estimate of pi : %i' % pi
    
    print 'Using str: %s' % 42L
    
    print 'Using repr: %r' % 42L
    
def widthAndPrecision():
    '''
    To show the width and precision of conversion specifier
    '''
    
    from math import pi
    print "%10f" % pi   # field width 10
    
    print "%10.2f" % pi # field width 10 and precision 2
    
    print "%.2f" % pi   # precision 2
    
    print "%.5s" % "Guido van Rossum"   # limit the length of string to output
    
    print "%.*s" % (5, "Guido van Rossum") # use it from the tuple instead of the template, making it constantable
    
def signsAligmentZeroPadding():
    '''
    Read func name
    '''
    from math import pi
    print "%010.2f" % pi        # put 0 to pad value with zero to take up the space
    
    print "%-10.2f" % pi        # put - to align the value to left.
    
    print ("% 5d" % 10) + '\n' + ("% 5d" % -10) # put a space for positive allowing negative nums to align with positive nums
    
    print "%+5d \n%+5d" % (5, -5)   # force put plus or minus
    
def strMethods():
    '''
    Experiment with strings
    '''
    
    print 'With a moo-moo here and a moo-moo there'.find('moo')       # find first index of given string
    
    print 'With a moo-moo here and a moo-moo there'.find('moo', 10)       # find first index of given string, but with a starting point
    
    print 'With a moo-moo here and a moo-moo there'.find('moo', 12, 15)   # find first index of given string, but with a starting point and ending point.
    
    ''''''
    seq = ['1', '2', '3', '4', '5', '6']
    ','.join(seq)   # joining a list of strings
    
    dirs = '', 'dirs', 'bin' , 'env'
    print '/'.join(dirs)
    
    print 'C:' + '\\'.join(dirs)
    
    '''Lower'''
    
    print 'T.G.I.F'.lower()     #use it for ci searches
    
    if 'Wally'.lower() in ['Wolly', 'Wally', 'Walry', 'Walrus']: print "Found him"
    
    '''Replace'''
    
    print 'I can has cheeseburger'.replace('has', 'haz')
    
    '''split()'''
    print "1,2,3,4,5".split(',')
    
    print 'Using     the    \nbla'.split()      # no arg to split using white space.
    
    '''strip() - to get rid of stuff before and after text
       lstrip()
       rstrip()
    '''
    print "     hahaha - ladada - blabla bla     ".strip()      # to strip whitespace
    print " ****** SPAM *** FOR EVERYONE!! ****".strip(' *!')   # to strip all chars specified
    
strMethods()