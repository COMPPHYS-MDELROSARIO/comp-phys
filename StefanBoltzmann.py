from math import exp, pi

def difference(curr_diff, last_diff):
    frac_diff = ((curr_diff - last_diff)/curr_diff)* 100
    return frac_diff, '%'

def summation(a, b, dy): #a and b are the bounds of integration
    n = 100.
    steps = 0
    y = 0
    area = 0
    
    print 'running...'
    while steps < b:
        while y < b:
            #Delta x
            delx = (b-a)/n
            length = (a + y*delx)
            area += (delx*length) * dy
            y += 1
        print 'number of steps:', '{:4.1f}'.format(steps*y)
        print 'dy =', '{0:.4f}'.format(dy), 'integral =', area
        print 'frac-diff ='
        steps += 1
        dy /= 2.
        y = 0

        
#if frac_diff <   
summation(0,100,1)

print 'The integral evaluated to within specified accuracy: ', '{0:.7f}'#.format(area)
print 'The upper limit of its fractional error is estimated to be: ', '{0:.7f}'.format(frac_diff)
print 'The correct answer is: ', '{:4.1f}'.format(pi**4/15)
print 'The actual fractional error is: ', '{0:.7f}'.format(frac_diff*100)
