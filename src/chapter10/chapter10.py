import sys, pprint
from heapq import heappush

def importTest():
    # import a module 
    import hello2
    
    # and use it
    hello2.hello()
    
    pprint.pprint(sys.path)

## Scripts below are best tested under scripting shell
'''
import copy

# use dir to explore contents of a module
print [n for n in dir(copy) if not n.startswith("_")]
print copy.__all__

## checking out help subjects
help(copy.copy)
print copy.copy.__doc__
'''

def setsTest():
    set(range(10))      # for testing membership, duplication ignored.
    #you can use standard operation too.
    a = set([1,2,3])
    b = set([2,3,4])
    
    assert a.union(b) == a | b, "This is union of sets"
    
    c = a & b               #intersection of sets
    assert c.issubset(a)
    
    assert c <= a           #boolean operation if c is "smaller" than a
    
    assert c.issuperset(a) == False
    assert a.issuperset(c), "This should be true"
    
    assert a.intersection(b) == a & b, 'This is intersection'
    
    assert a.difference(b) == a - b, 'This is difference'
    
    assert a.symmetric_difference(b) == a ^ b, 'This is symmetric difference'
    
    assert (a.copy() is a) == False, 'They don\'t point to the same mem location'
    
def setsReduce():
    '''
    A demostration of using unbound set.union method to reduce a set
    '''
    mySets = []
    for i in range(10):
        mySets.append(set(range(i, i+5)))
        
    pprint.pprint(mySets)
    print reduce(set.union, mySets)



def heapsTest():
    '''
    All tests for heaps
    import the following first in module level.
    from heapq import *
    from random import shuffle
    '''
    from heapq import heappop, heapify
    from random import shuffle   
    
    data = range(10)
    shuffle(data)
    heap = []
    for n in data:
        heappush(heap, n)
        
    print heap
    
    heappush(heap, 0.5)
    print heap
    
    print heappop(heap)
    print heappop(heap)
    print heappop(heap)
    
    heap2 = [2,3,9,5,6,12,7,12,13,17,3,2,7]
    heapify(heap2)
    print heap2
    print heappop(heap2)
    
def dequesTest():
    '''
    Testing double ended ques
    '''
    from collections import deque
    q = deque(range(5))
    q.append(5)
    q.appendleft(6)
    print q
    print q.popleft()
    q.rotate(3)
    print q

    q.rotate(-1)
    print q
    

def randomTest():
    '''
    Testing functions of random module.
    '''
    from random import uniform, randrange
    from time import mktime, localtime, asctime
    
    date1 = (2008, 1,1,0,0,0,-1, -1,-1)
    time1 = mktime(date1)
    
    date2 = (2009, 1,1,0,0,0,-1,-1,-1)
    time2 = mktime(date2)
    
    random_time = uniform(time1, time2)
    print asctime(localtime(random_time))
    
    num = input("How many dice? ")
    sides = input("How many sides per dice? ")
    sum = 0
    for i in range(num) : sum += randrange(sides) + 1
    print 'The result is', sum
     

def cardsTest():
    '''
    cards dealer test code
    '''
    from pprint import pprint
    from random import shuffle
    
    values = range(1,11) + "Jack Queen King".split()
    suits = "daimonds clubs hearts spades".split()
    deck = ["%s of %s" % (v,s) for v in values for s in suits]
    shuffle(deck)
    pprint(deck[:12])
    ##to deal deck.pop()
    
