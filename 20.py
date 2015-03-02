'''Find the sum of the digits in the number 100!'''

from math import factorial

print sum(map(int,str(factorial(100))))

n = 1
i = 2
while i <= 100:
    n *= i
    i += 1

print sum(map(int,str(n)))

L = [1]
i = 2
while i <= 100:
    carry = 0
    for j in xrange(len(L)):
        L[j] = L[j]*i + carry
        carry = L[j]/10
        L[j] %= 10
    if carry:
        L.append(carry)
    #print ''.join(str(c) for c in L[::-1])
    i += 1
if L[-1] >= 10:
    g = map(int,str(L[-1]))

    L.pop()
    L.extend(g[::-1])
    
print sum(L)
