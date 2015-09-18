"""

>>> gamma(3)
2
>>> gamma(8)
5040
>>> gamma(3.5)
3.32335
>>> gamma(5.5)
52.3428

The gamma() function takes a value of t and depending on if it is a float or not will decide whether to use
gamma_factorial or gamma_integral. If it is a decimal it will call gamma_factorial. If it is a float, it will
call gamma_integral.


"""

from math import exp
from math import factorial 

def gamma_factorial(t):
    if t >= 1:
        fact = factorial(t - 1)
    return fact

def gamma_func(x, t, dx = 0.5):
    return x**(t-1) * (exp(-x))*dx
    

def gamma_integral(t, a = 0, b = 1000, dx = 0.5):
    total_area = 0
    n = int((b-a)/dx)
    for y in range(0, n+1):
        x1 = a + (y-1) * dx
        x2 = a + y * dx
        
        rect_area = ((gamma_func(x1, t) + gamma_func(x2, t)) / 2.) * dx
        
        total_area += rect_area

    return total_area
    
def gamma(t):
    if t % 1 == 0:
        print gamma_factorial(t)
    else:
        print gamma_integral(t)
        

gamma(5)
        
    
if __name__ == "__main__":
    
    import doctest
    #doctest.testmod()
    
    