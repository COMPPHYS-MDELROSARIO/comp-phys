import datetime as dt
import random
import numpy as np
import pdb as p
import urllib
import re

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
    
    def name(self):
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
            
            if self.sex() == 'male':
                return random.sample(male_names, 1)[0]
            else:
                return random.sample(female_names, 1)[0]

    
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
                namefromlist.Dolphins(namefromlist, dolphs, dolphs, sex_prob)
            
            
            
            
    

#d1 = Dolphins('hi')

