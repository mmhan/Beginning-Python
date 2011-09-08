#all the examples in trial

def slicingLists():
    '''
    various ways of slicing lists.
    '''
    
    tag = '<a href="http://mmhan.net/">My Website</a>'
    
    print tag[9:25] #simple way of slicing <start:inc>:<end:exclusive>
    
    print tag[28:-4] #<end> can be -x of length too.
    
    numbers = range(1,11)
    
    print numbers[7:10]
    
    print numbers[-3:-1] #get the 3rd and 2nd last.
    
    print numbers[-1:] #<end> can be ignored too.
    
    print numbers[:3] #and also <start>
    
    copyOfNumbers = numbers[:] #this is how you can copy a list.
    
    print copyOfNumbers 
    
    '''
    You can also do steps
    '''
    
    print numbers[::2] #index+2 items from index 0
    
    print numbers[::-2] #minus in step will extract element from right to left;
    
    print numbers[::-1] #to reverse a list
    
        
    print numbers + copyOfNumbers #concat
    print numbers[9:] * 5 # multiply
    
    sequence = [None] * 10 #init a list of length 10
    print sequence
    
    print    

def membership():
    '''
    To check membership of an element in a list or string
    '''
    
    permissions = 'rw'
    print 'r' in permissions
    print 'x' in permissions
    
    users  = ['foo', 'bar', 'foobar']
    if raw_input("Username : ") in users:
        print "Valid user"
    else:
        print "Invalid user"   
    
    str = "Python rocks"
    
    print "Does Python rocks?"
    print "rocks" in str # will only work in later versions of python
    print
    
    
def lenMinMax():
    '''
    To get length, min and max values of a list
    '''    
    
    numbers = range(1,11)

    print len(numbers)
    print min(numbers)
    print max(numbers)

def strToList(str):
    '''
    Will turn any string into list
    '''
    return list(str)


'''

del lst[index] # to delete an element 
del lst[<start>:<end>] # to delete a slice

lst[index] = <something>
lst[<start>:<end>] = [] #to delete a section
lst[<start>:<end>] = [<bigger list>] # to expand

'''

def listMethods():
    '''
    Testing out the list methods
    '''
    lst = range(1, 4)
    lst.append(4)
    print lst
    lst.append([5,6]) # to append whatever item that's given to the end of the list as it is. for case of x[<outOfIndex>] = 'bla' and growing collection of stuff.
    print lst
    
    quote = ['to', 'be', 'or', 'not', 'to', 'be']
    print quote.count('to') #to count occurence of certain element in a list.
    
    lst = range(5,11)
    lst.extend([11, 12]) #to extend a list with elements of another list.
    print lst
    
    print lst.index(11) #to find index of an element
    print quote.index('not')
    
    
    lst.insert(3, 'four') #to insert an element at given index. alternative to lst[3:3] = 'four'
    print lst
    
    ''' Great for implementing a stack '''
    x = [1,2,3]
    print x.pop()       #pop last in list #This is the only method that modifies the list AND return value.
    print x.pop(1)      #pop given index in list
    ''' --- ''' 
    
    quote.remove("not") # to remove a given element out of given list
    
    x = [1,2,3]
    x.reverse()         # to reorder the list in reverse, modify the list
    reversed(x)         # return iterator to use in list() function as argument
    
    x.sort()            # sorts and modifies the list to be in order, no return
    print sorted(x)     # sorted() returns value, and does not chage list.
    
    #sort(cmp) to provide custom sorting function
    #    where cmp is cmp(x,y)
    #        returns -1 on x < y
    #                1  on x > y
    #                0  on x = y
    
    # x.sort(key = <function>) to generate sorting key using given function with element
    # e.g x.sort(key = len) where x is a list of string elements
    
    # x.sort(reverse = true) to make it decending.
    
    # more on http://python.org/doc/howto


# slicingLists()
# membership()
# lenMinMax()
# print strToList(raw_input("Give me something : "))

listMethods()



raw_input("Press <enter> to exit.")