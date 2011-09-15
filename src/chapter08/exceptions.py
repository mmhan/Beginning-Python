#!usr/bin/python2

def raiseException():
    raise Exception

def raiseExceptionWithStr():
    raise Exception, 'Hyperdrive overload'

def raiseExceptionWithStrArg():
    raise Exception('Hyperdrive overload')

def findExceptions():
    import exceptions
    dir(exceptions)
    
def catchException():
    try:
        x = input("Enter the first number : ")
        y = input("Enter the second number : ")
        print x / y
    except ZeroDivisionError:
        print "The second number can't be zero!"
        
class MuffledCalculator:
    muffled = 0
    def calc(self, expr):
        try:
            return eval(expr)
        except ZeroDivisionError:
            if self.muffled:
                print 'Division by zero is illegal'
            else: raise
        except TypeError:
            print "That wasn't a number, was it?"
        except (ArithmeticError, AssertionError):
            print "This is catching two birds with one stone."
        except AttributeError, e:       # catching the exception itself for logging
            print e
        except:
            print "Something wrong happened..."
        else:
            print "Ah... it went alright."
            
        #finally: will be executed no matter what happened