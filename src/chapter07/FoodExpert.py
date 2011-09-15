#!usr/bin/python2

class FoodExpert:
    def init(self):
        self.goodFood = []
        
    def addGoodFood (self, food):
        self.goodFood.append(food)
        
    def likes(self, food):
        return food in self.goodFood
    
    def prefers(self, x, y):
        x_rating = self.goodFood.index(x)
        y_rating = self.goodFood.index(y)
        
        if x_rating > y_rating:
            return y
        else:
            return x
        
f = FoodExpert()
f.init()
map(f.addGoodFood, ['SPAM', 'Eggs', 'Bacon', 'Rat', 'Spring Surprise'])

print f.goodFood

menu = ['Filet Mignon', 'Pasta', 'Pizza', 'Eggs', 'Bacon', 'Tomato', 'SPAM']
rec = filter(f.likes, menu)
print rec

