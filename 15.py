'''Starting in the top left corner of a 2x2 grid, and only being able to move
to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there in a 20x20 grid?'''

# realize the answer is 40!/(20! * 20!) = ^{40}C_{20}
# basically it is the num of permutations of 20 R and 20 D

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
    return comb(n-1,k-1)*n/k if k > 0 else 1

def comb_2(n,k):
    return comb(n,k-1)*(n+1-k)/k if k > 0 else 1

def comb_3(n,k):
    return comb(n-1,k) + comb(n-1, k-1) if k > 0 else 1

print(fact(40)/fact(20)/fact(20))
print(iter_fact(40)/iter_fact(20)/iter_fact(20))
print(factorial(40)/factorial(20)/factorial(20))
print(comb(40,20))
print(comb_2(40,20))
print(comb_3(40,20))
