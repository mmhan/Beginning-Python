#!usr/bin/python2

class Filter:
    '''
    Filter class to inherit
    '''
    def init(self):
        self.blocked = []
        
    def filter(self, sequence):
        return [x for x in sequence if x not in self.blocked]
    
class SPAMFilter(Filter):
    '''
    Spam filter that filter out SPAM
    '''
    def init(self):
        self.blocked = ['SPAM']

def investigateSubclasses():        
    '''
    investigating subclasses
    '''
    print issubclass(SPAMFilter, Filter)
    print issubclass(Filter, SPAMFilter)
    
    print SPAMFilter.__bases__
    
    s = SPAMFilter()
    print s.__class__ is SPAMFilter


# Multiple Super classes
class Calculater:
    '''
    eval a given expression
    '''
    def calculate(self, expression):
        '''
        Eval a given expression and store it as self.value
        '''
        self.value = eval(expression)

class Talker:
    '''
    Speak its own value
    '''
    def talk(self):
        '''
        print its own value
        '''
        print 'Hi, my value is ', self.value
        
class TalkingCalculator(Calculater, Talker):
    pass

def multipleSuperClasses():
    tc = TalkingCalculator()
    tc.calculate("3 + 5")
    tc.talk()
    
    # checking for existence of an attribute
    print hasattr(tc, 'talk')
    print hasattr(tc, 'talkaa')
    print callable(getattr(tc, 'talk', None))
    print callable(getattr(tc, 'talkaa', None))

multipleSuperClasses()