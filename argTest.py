# argparse breakout

"""
>>> tempConversion(0)
32.0
>>> tempConversion(1)
33.8
>>> tempConversion(2)
35.6

Call signature :

python argTest.py -x 2. 
    
    To run doctests in verbose mode:
    
    python -m doctest -v argTest.py
"""


def tempConversion(x):
    Fdegrees = (9.0/5)*x + 32.
    return Fdegrees

#print tempConversion(2)

if __name__ == "__main__":
    
    import doctest
    import argparse
    #doctest.testmod()
    
    
    
    parser = argparse.ArgumentParser()
    parser.add_argument('-x', type = float)
    args = parser.parse_args()
    x = args.x
    print 'Temp in Farenheit is', tempConversion(x)