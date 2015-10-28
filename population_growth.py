"""
This program takes 4 initial dolphins and has them procreate under certain conditions. It does 10 trials,
all spanning to 149 years and lists the current dolphin population and how many are currently breeding.
It also takes into account dolphins that have died and has strict prerequisites for procreation such as
age, relation, sex, and if the dolphins hae mated within 5 years.
"""

import random
import numpy as np
import os.path
import urllib
import re
from pdb import set_trace


#This function properly assigns the male name to the male dolphin and the female name to the female dolphin
#It also creates the instance of the baby dolphin and starts the count which tracks the time before
#either dolphin can mate again
def procreate(male_dolphs, female_dolphs, spouse1, spouse2, male_namer, female_namer):
    if spouse1.sex == 'male':
        malespouse = spouse1.name
    else:
        femalespouse = spouse1.name
    if spouse2.sex == 'male':
        malespouse = spouse2.name
    else:
        femalespouse = spouse2.name
    if spouse1.can_mate(spouse2) == True:
        kid_sex = random.sample(['male', 'female'], 1)[0]
        if kid_sex == 'male':
            kid_name = male_namer.next()
            male_dolphs[kid_name] = Dolphins(kid_name, kid_sex, malespouse, femalespouse)
            malespouse.can_give_birth = 0
            femalespouse.can_give_birth = 0
        else:
            kid_name = female_namer.next()
            female_dolphs[kid_name] = Dolphins(kid_name, kid_sex, malespouse, femalespouse)
            malespouse.can_give_birth = 0
            femalespouse.can_give_birth = 0

#This function generates the name for the baby dolphin based on the gender
#It gathers both male and female names from a website and writes them to a text file which is saved locally
def name_generator(sex):
    count = 1
    count2 = 1
    a = 0
    b = 0
    male_names = []
    female_names = []

    filenm = 'males.txt'
    filenm2 = 'females.txt'
    
    #set_trace()
    if os.path.isfile('males.txt') == True:
        ''
    else:
        while count < 226:
            url1 = 'http://www.prokerala.com/kids/baby-names/boy/page-'+str(count)+'.html'
            infile1 = urllib.urlopen(url1)      
            lines1 = infile1.readlines()
            infile1.close()

            for line1 in lines1:
                m1 = re.search("(nameDetails\">)([A-Z].*[a-z])<", line1)
                if m1:
                    male_names.append(m1.group(2))
            count += 1
            
        with open(filenm,"w") as f:
            f.write(str(male_names))
                    
    if os.path.isfile('females.txt') == True:
        ''
    else:
        while count2 < 171:
            url2 = 'http://www.prokerala.com/kids/baby-names/girl/page-'+str(count2)+'.html'
            infile2 = urllib.urlopen(url2)      
            lines2 = infile2.readlines()
            infile2.close()
            
            for line2 in lines2:
                m2 = re.search("(nameDetails\">)([A-Z].*[a-z])<", line2)
                if m2:
                    female_names.append(m2.group(2))
            count2 += 1
            
        with open(filenm2,"w") as f:
            f.write(str(female_names))

   
    if sex == 'male':
        set_trace()
        while a < len(eval(filenm)):
            f = open(filenm, 'r')
            yield eval(f.read())[a]
            a += 1
    if sex == 'female':
        while b < len(eval(filenm2)):
            f = open(filenm2, 'r')
            yield eval(f.read())[b]
            b += 1
            

class Dolphins:
    def __init__(self, name, sex, mother, father):
        self.name = name
        self.mother = mother
        self.father = father
        self.sex = sex
        self.age = 0
        self.death = random.gauss(35, 5)
        self.can_give_birth = 0

    #Increases the age of the dolphin each timee it is called
    def dolph_age(self):
        self.age += 1
        self.can_give_birth += 1
    
    #This function checks the eligibility of a dolphin to mate           
    def can_mate(self, spouse):
        if spouse.age < 8\
        or self.age < 8\
        or self.mother == spouse.mother\
        or self.father == spouse.father \
        or np.absolute(self.age - spouse.age) > 10\
        or self.can_give_birth < 5\
        or spouse.can_give_birth < 5\
        or self.age >= self.death\
        or spouse.age >= self.death:
            return False
        else:
            return True
                    
                

alive = []
male_dolphs = []
female_dolphs = []

#This loop makes sure that the lengths are all the same
for k in range(0,10):
    male_dolphs.append(''+str(k))
    female_dolphs.append(''+str(k))
    alive.append(''+str(k))
    
#This block of code starts the 10 trials all spanning 150 years
#Also takes into account the amount of total dolphins, dead dolphins, and currently breeding dolphins
#Updates the user every 25 years with the dolphin population information
for x in range(0, 10):    
    male_dolphs[x] = {'James':Dolphins('James', 'male', '', '') , 'John':Dolphins('John', 'male', '', '')}
    female_dolphs[x] = {'Mary':Dolphins('Mary','female', '', '' ), 'Patricia':Dolphins('Patricia','female', '', '' )}
    male_namer = name_generator('male')
    female_namer = name_generator('female')
  
    print 'Trial No.', x+1
    dead = []
    time_years = 0
    alive[x] = []
    
    while time_years < 150:
        male_dolph_names = male_dolphs[x].keys()
        female_dolph_names = female_dolphs[x].keys()
        
        for guys in male_dolph_names:
            for wife in female_dolph_names:
                fam = procreate(male_dolphs[x], female_dolphs[x], male_dolphs[x][guys], female_dolphs[x][wife], male_namer, female_namer)
        for dead_dolphs in male_dolph_names:
            male_dolphs[x][dead_dolphs].dolph_age()
            if male_dolphs[x][dead_dolphs].age >= male_dolphs[x][dead_dolphs].death and dead_dolphs not in dead:
                dead.append(dead_dolphs)
        for dead_dolphs in female_dolph_names:
            female_dolphs[x][dead_dolphs].dolph_age()
            if female_dolphs[x][dead_dolphs].age >= female_dolphs[x][dead_dolphs].death and dead_dolphs not in dead:
                dead.append(dead_dolphs)
        updated_male_dolphs = male_dolphs[x].keys()
        updated_female_dolphs = female_dolphs[x].keys()
        current_dolphs = len(updated_male_dolphs) + len(updated_female_dolphs) - len(dead)
        alive.append(current_dolphs)
        
        
        if time_years % 25 == 0:
            print 60*'#'
            print 'Entering year {:d} with {:d} dolphins, with {:d} breeding.'.format(time_years, current_dolphs, \
                                                                                      abs(len(updated_male_dolphs)+len(updated_female_dolphs)\
                                                                                         - len(male_dolph_names) - len(female_dolph_names)))
        if time_years == 100:
            print 'At year {:d}, there are {:d} living dolphins.'.format(time_years, current_dolphs)
            print 'There have been {:d} births in total'.format(len(male_dolph_names) + len(female_dolph_names) - 4)
        if time_years == 149:
            print 60*'#'
            print 'At year {:d}, there are {:d} living dolphins.'.format(time_years, current_dolphs)
        
        time_years += 1

#This block of code calculates the standard deviation of the dolphin population and plots it
#stand_dev = []
#for a in range(0, 150):
#    stand_dev.append((np.mean([b][a]for b in alive), np.std([b][a] for b in alive)))
#plus_stand_dev = [a + b for a, b in stand_dev]
#minus_stand_dev = [a - b for a, b in stand_dev]
#average = [a[0] for a in stand_dev]
#
#plt.title('Average Population and Standard Deviation from 10 Trials')
#plt.xlabel('Years')
#plt.ylabel('Number of living Dolphins')
#x = np.arange(0, time_years, 1)
#plt.plot(x, average, 'r')
#plt.fill_between(x, minus_stand_dev, plus_stand_dev)
#plt.show()