'''
HW03
Matthew del Rosario
Matthew Español


Asks the user to enter the range at which the prime numbers should be found.
Prints all prime numbers within the range given by the input.
'''


import numpy as np

def prime(a, b):
    prime_range = np.arange(a,b)

    for num in prime_range:
        prime = True
        for i in range(2,num):
            if (num%i==0):
                prime = False
        if prime:
           print num

a, b = input("Please enter a range of numbers (a,b):" )
prime(a,b)