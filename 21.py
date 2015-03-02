''' Let d(n) be defined as the sum of proper divisors of n.
If d(a) = b and d(b) = a, a != b, then a and b are an amicable pair

and each of them is an amicable number.

Evaluate the sum of all amicable numbers under 10000.'''

def sum_divisors(n):
    div = 2
    s = 0
    while div*div <= n+1:
        if div >= n:
            break
        if n%div == 0:
            if n/div == div:
                s += div
            else:
                s += div + n/div
        div += 1
    return s+1

def is_amicable(n):
    a = sum_divisors(n)
    if n == sum_divisors(a) and a != n:
        return True

s = 0
amicable_list = []
for n in xrange(2,10000):
    if is_amicable(n):
        s += n
        amicable_list.append(n)
print s
