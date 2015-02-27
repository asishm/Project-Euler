'''There exists only one Pythagorean triplet (a,b,c) where a + b + c = 1000

(a,b,c) is a triplet if a < b < c and a^2 + b^2 = c^2 and a,b,c are natural no.

Find the product abc'''

for c in xrange(1,1000):
    for b in xrange(1,min(c,1000-c+1)):
        a = 1000 - b - c
        if a**2 + b**2 - c**2 == 0:
            print a*b*c, a,b,c
            break
