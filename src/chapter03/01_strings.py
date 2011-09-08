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
    
strTemplate()