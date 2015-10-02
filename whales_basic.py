'''
Creates 20 instances of the whale class each with a different name and a 50% chance of being either male or female
'''
import datetime as dt
import random

class whale:
    def __init__(self, name, sex):
        self.name = name
        self.sex = sex
        self.birth = dt.datetime.now()

        if self.sex == 'M':
            sex = "male"
        elif self.sex == 'F':
            sex = "female"
        print 'A {:s} whale named {:s} has been born!'.format(self.sex, name)
        
    def age(self):
        self.newage = dt.datetime.now() - self.birth
        return self.newage

    def sing(self):
        return 5*'\a'
    def __str__(self):
        return 'A whale named {:s} age {:s}'.format(self.name, self.age())
    



whales = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't']    
names = []    

count = 0
while count < len(whales):
    sex = random.sample(['male', 'female'], 1)[0]
    names.append(whale(whales[count], sex))
    #whales[count] = whale(whales[count], sex)
    count += 1
    
    