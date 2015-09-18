from math import exp as m
"""

>>> gamma_factorial(3)
2
>>> gamma_factorial(8)
5040
>>> gamma_integral(3.5)
3.32335
>>> gamma_integral(5.5)
52.3428

"""
from math import factorial 
from pprint import pprint

def gamma_factorial(t):
    if t >= 1:
        fact = factorial(t - 1)
    return fact

def gamma_func(x, t, dx = 0.5):
    return x**(t-1)*m.exp(-x)*dx
    

def gamma_integral(a = 0, b = 1000, dx = 0.5):
    total_area = 0
    n = int((b-a)/dx)
    for y in range(0, n+1):
        x1 = a + (y-1) * dx
        x2 = a + y * dx
        
        rect_area = ((gamma_func(x1) + gamma_func(x2)) / 2) * dx
        
        total_area += rect_area
    return total_area
    
#pprint(gamma_factorial(4))

def gamma(t):
    if type(t) == int:
        gamma_factorial(t)
    else:
        gamma_integral()
        

gamma(3)        
        
    
if __name__ == "__main__":
    
    import doctest
    doctest.testmod()
    
    
    