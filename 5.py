'''What is the smallest positive number that is evenly
divisible by all of the numbers from 1 to 20?'''

from fractions import gcd
print reduce(lambda x,y: x*y/gcd(x,y), xrange(1,21))
