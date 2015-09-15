"""
>>> tempConversion(0)
32.0
>>> tempConversion(1)
33.8
>>> tempConversion(2)
35.6
"""


def tempConversion(x):
    Fdegrees = (9.0/5)*x + 32.
    print Fdegrees

tempConversion(2)

if __name__ == "__main__":
    
    import doctest
    doctest.testmod()
    