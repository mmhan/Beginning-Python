# everything about tuples.

def initTuples():
    '''
    To initiate tuples
    '''
    
    tuple([1,2,3])  #using list
    tuple('foo')    #using string
    tuple((1,2,3))  #using tuple, no change
    
    x = 1,2,3       #make a new tuple
    x[1]            #access it
    x[0:2]          #slice it, to get another tuple
    
#tuples can be keys to map, lists can't
#built-in functions and methods reutrn them.