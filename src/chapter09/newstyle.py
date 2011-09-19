#!usr/bin/python2

__metaclass__ = type

class Bird:
    def __init__(self):
        self.hungry = True
    def eat(self):
        if self.hungry:
            print "Aaah..."
            self.hungry = False
        else:
            print "No Thanks."
            
class SongBird(Bird):
    def __init__(self):
        
        #calling the unbound superclass constructor
        #Bird.__init__(self);
        
        #using super (more preferable)
        super(SongBird, self).__init__()
        self.sound = 'Squawk!'
        
    def sing(self):
        print self.sound
        
    '''
    Others
    
    __len__(self): to return number of items contained in the collection
    
    __nonzero__(self): to return or not to return zero as length
    
    __getitem__(self, key): to return the value of key
    
    __setitem__(self, key, value): to set the value of key in mutable objects
    
    __delitem__(self, key): to delete the value of key in mutable objects
    
    '''
        
def checkIndex(key):
    '''
    Is the given key an acceptable index?
    
    To be acceptable, the key should be a non-negative integer. If it
    is not an integer, a TypeError is raised; if it is negative, an IndexError
    is raised (since the sequence is infinite0
    '''
    if not isinstance(key, (int, long)): raise TypeError
    if key < 0: raise IndexError
    
class ArithmeticSequence:
    def __init__(self, start = 0, step =1):
        '''
        Initialize the arithemetic sequence.
        
        start       - the first val in the sequence
        step        - the difference between two adjacent values
        changed     - a dictionary of values that have been modified by the user
        '''
        self.start = start  #store the start
        self.step = step    #store the step
        self.changed = {}   #init the dict for changed values
        
    def __getitem__(self, key):
        '''
        Get an item from the arithmetic sequence
        '''
        checkIndex(key)
        
        try: return self.changed[key]           #modified?
        except KeyError:                        #otherwise
            return self.start + self.step * key #calculate the value
        
    def __setitem__(self, key, value):
        '''
        set an item in the arithmetic sequence
        '''
        self.changed[key] = value               #store changed value
        

class CounterList(list):
    '''
    An example list object (or type) that keeps track of 
    how many times __getitem__ has been called.
    '''
    
    def __init__(self, *args):
        super(CounterList, self).__init__()
        self.counter = 0
        
    def __getitem__(self, index):
        self.counter += 1
        return super(CounterList, self).__getitem__(index)
        

class Rectangle:
    def __init__(self):
        self.width = 0
        self.height = 0
    def setSize(self, size):
        self.width, self.height = size
    def getSize(self):
        return self.width, self.height
    
    size = property(getSize, setSize) # by adding this line it lets client code do something like "rect.size = width, height"
    
    
def generatorTest():
    for i in range(10):
        yield i
        #when yield is used the scope is frozen and remembered
        #the var that follows yield is returned
        #when it is reused the scope is reused to generate another number.
        
print list(generatorTest())     #will generate a list of 0-9 by calling next at all times,