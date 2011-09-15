#!usr/bin/python2

def factorial(n):
    '''
    find factorial of given n, recursive
    '''
    if n == 1: return 1
    else: return n * factorial(n-1)
    
def power(x, n):
    '''
    find power x in n, recursive
    '''
    if n == 0: return 1
    else: return x * power(x, n - 1)
    
def search(sequence, number, lower = 0, upper = None):
    '''
    Bisection method to search for a number in sorted sequence
    '''
    if upper is None: upper = len(sequence) - 1
    if lower == upper:
        assert number == sequence[upper]
        return upper
    else:
        middle = (lower + upper) // 2
        if number > sequence[middle]:
            return search(sequence, number, middle, upper)
        else:
            return search(sequence, number, lower, middle)
        
def mapFns():
    '''
    Testing map functions, use list comprehension if you like. it's about the same. (Map are builtin hence, faster)
    '''
    numbers = [72,101,108,108,111,44,32,119,111,114,108,100,33]
    print map(lambda n: 2*n, numbers)
    
    print map(chr, numbers)
    
    print map(ord, "Hello, World!")
    
def filterFns():
    '''
    Testing filter function, use list comprehension if you like, it's about the same. (filter is builtin functions, faster)
    '''
    numbers = [72,101,108,108,111,44,32,119,111,114,108,100,33]
    print filter(lambda n: n % 2 == 0, numbers)
    
def reduceFns():
    '''
    Testing reduce function.
    reduce put in n and n+1 into function given til the end of the sequence
    '''
    numbers = [72,101,108,108,111,44,32,119,111,114,108,100,33]
    print reduce(lambda x,y: x + y, numbers)    # equivalent of sum()
    
    print reduce(max, numbers)                  # finding the maximum val in sequence
    
def applyFns():
    '''
    Takes function as parameter and arguments as another parameter to call the function.
    '''
    
    def rectangleArea(width, height):
        return width * height
    
    rectangle = 20, 30
    print apply(rectangleArea, rectangle)