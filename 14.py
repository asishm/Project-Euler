'''The following iterative sequence is defined for the set
of positive integers:

n -> n/2 (n is even)
n -> 3n+1 (n is odd)

Which starting number, under one million, produces the longest chain?
'''

import time

st = time.time()

n = 1

generated = {1:1, 2:2}
start, chain = 1,1
for s in xrange(3,1000000):
    c = 0
    g = []                         # terrible variable names, i know
    n = s
    while n not in generated:
        g.append(n)
        if n%2:
            n = 3*n+1
        else:
            n = n/2
        c += 1
    d = generated[n]
    for k, m in enumerate(g):
        generated[m] = d + c - k
    if d + c >= chain:
        chain = d + c
        start = s
    
print (time.time() - st)
print start
