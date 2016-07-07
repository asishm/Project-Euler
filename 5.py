'''What is the smallest positive number that is evenly
divisible by all of the numbers from 1 to 20?'''

from fractions import gcd
import functools
print(functools.reduce(lambda x,y: x*y/gcd(x,y), range(1,21)))
