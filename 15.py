'''Starting in the top left corner of a 2x2 grid, and only being able to move
to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there in a 20x20 grid?'''

# realize the answer is 40!/(20! * 20!) = ^{40}C_{20}
# basically it is the num of permutations of 20 R and 20 D
import time
d = {1:1}

def fact(n): # recursive factorial .. can have recursion limit error
    if n not in d:
        d[n] = n*fact(n-1)
    return d[n]

def iter_fact(n): # does not suffer from stack overflow
    if n not in d:
        for j in range(max(d.keys())+1,n+1):
            d[j] = j*d[j-1]
    return d[n]

from math import factorial # built-in

def comb(n,k):
    return int(comb(n-1,k-1))*n/k if k > 0 else 1

def comb_2(n,k):
    return int(comb(n,k-1))*(n+1-k)/k if k > 0 else 1

def comb_3(n,k):
    return int(comb(n-1,k)) + int(comb(n-1, k-1)) if k > 0 else 1

iter_d = {0:1, 1:1}
def iter_comb(n, k):
    max_fact = max(k, n-k)
    prod = 1
    for j in range(max_fact+1, n+1):
        prod *= j
    if max_fact not in iter_d:
        for j in range(max(iter_d)+1, max_fact+1):
            iter_d[j] = j*iter_d[j-1]
    return prod//iter_d[max_fact]

size = 10000

##try:
##    start = time.time()
##    print(fact(2*size)//(fact(size)**2))
##    print(time.time() - start, '\n==========================')
##except Exception as e:
##    print("method 1 failed", e, "\n======================")

try:    
    start = time.time()
    print(iter_fact(2*size)//(iter_fact(size)**2))
    print(time.time() - start, '\n==========================')
except Exception as e:
    print("method 2 failed", e, "\n======================")

try:    
    start = time.time()
    print(factorial(2*size)//(factorial(size)**2))
    print(time.time() - start, '\n==========================')
except Exception as e:
    print("method 3 failed", e, "\n======================")

try:    
    start = time.time()
    print(iter_comb(2*size, size))
    print(time.time() - start, '\n==========================')
except Exception as e:
    print("method iter_comb failed", e, "\n======================")

try:    
    start = time.time()
    print(comb(2*size,size))
    print(time.time() - start, '\n==========================')
except Exception as e:
    print("method 4 failed", e, "\n======================")

try:    
    start = time.time()
    print(comb_2(2*size,size))
    print(time.time() - start, '\n==========================')
except Exception as e:
    print("method 5 failed", e, "\n======================")

try:    
    start = time.time()
    print(comb_3(2*size,size))
    print(time.time() - start, '\n==========================')
except Exception as e:
    print("method 6 failed", e, "\n======================")
