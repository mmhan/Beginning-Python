#!user/bin/python2

class Person:
    def setName(self, name):
        self.name = name
        
    def getName(self):
        return self.name
    
    def greet(self):
        print "Hi! I am", self.name
        
foo = Person()
bar = Person()
foo.setName("Luke Skywalker")
bar.setName("Anakin Skywalker")
foo.greet()
bar.greet()