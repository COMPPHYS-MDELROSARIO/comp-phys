import datetime as dt
import random
import numpy as np
import pdb as p

class Dolphins:
    def __init__(self, name, mother, father, sex, age = 0):
        self.name = name
        #self.sex = random.sample(['male', 'female'], 1)[0]
        #self.birth = dt.datetime.now()
        #print 'A {:s} dolphin named {:s} has been born!'.format(self.sex, name)
        self.mother = mother
        self.father = father
        self.sex = sex
        self.age = age
    
    def dolph_age(self):
        self.age += 1
        return self.age
    
    def procreate(self, dolphs):
        can_mate = True
        dad = False
        mom = False
        sex_prob = random.sample(['male', 'female'], 1)[0]
        new_male = ''
        new_female = ''
        while dad == False or mom == False:
            if random.sample(dolphs, 1)[0].sex == 'male':
                new_male = random.sample(dolphs, 1)[0]
                dad = True
            if random.sample(dolphs, 1)[0].sex == 'female':
                new_female = random.sample(dolphs, 1)[0]
                mom = True
        while can_mate == True:
            if self.age < 8 or new_male.mother == new_female.mother or new_male.father == new_female.father \
            or np.absolute(new_male.age - new_female.age) > 10:
                can_mate = False
            '''
            if self.age < 8:
                can_mate = False
            if new_male.mother == new_female.mother or new_male.father == new_female.father
                can_mate = False
            if np.absolute(new_male.age - new_female.age) > 10:
                can_mate = False
            '''
            else:
                namefromlist.Dolphins(namefromlist, dolphs, dolphs, sex_prob)
            
            
            
            
    

d1 = Dolphins('hi')