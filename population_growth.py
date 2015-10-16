import datetime as dt
import random
import numpy as np
import pdb as p
import urllib
import re

class Dolphins:
    count = 1
    
    for time in range(0,150):
        dolphs = 4
        if time % 25 == 0:
            print 'Entering year {:d} with ', dolphs, ', with {:d} breeding'.format(time,mjde)

    def __init__(self, name, mother, father, sex, age = 0):
        self.name = name
        self.mother = mother
        self.father = father
        self.sex = sex
        self.age = age
        self.can_give_birth = True

    #Increases the age of the dolphin each timee it is called
    def dolph_age(self):
        self.age += 1
        return self.age
    
    #Gets the list of names from the website and appends them to a list based on gender
    def name_generator(self):
        count = 1
        male_names = []
        female_names = []
        
        while count < 2:
            url1 = 'http://www.prokerala.com/kids/baby-names/boy/page-'+str(count)+'.html'
            url2 = 'http://www.prokerala.com/kids/baby-names/girl/page-'+str(count)+'.html'
            infile1 = urllib.urlopen(url1)      
            lines1 = infile1.readlines()
            infile1.close()

            infile2 = urllib.urlopen(url2)      
            lines2 = infile2.readlines()
            infile2.close()

            for line1 in lines1:
                m1 = re.search("(nameDetails\">)([A-Z].*[a-z])<", line1)
                if m1:
                    male_names.append(m1.group(2))

            for line2 in lines2:
                m2 = re.search("(nameDetails\">)([A-Z].*[a-z])<", line2)
                if m2:
                    female_names.append(m2.group(2))
            count += 1
            
            if self.sex == 'male':
                return male_names[count - 1]
            else:
                return random.sample(female_names, 1)[0]
            
    #Determines if 5 years have passed after a dolphin has mated
    def possible(self):
        if self.can_give_birth == True:
            self.can_give_birth = False
            return ("can give birth")  
        if self.can_give_birth == False:
            self.__class__.count += 1
            if self.__class__.count > 5:
                self.can_give_birth = True
                self.__class__.count = 1
                
    
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
            else:
                name.Dolphins(name(), dolphs, dolphs, sex_prob)
            
            
            
            
    

d1 = Dolphins('hi', '', '', 'male')
