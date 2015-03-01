'''Find the sum of all primes below 2 million'''

def sum_primes_to_n_naive(n):
    p = [2]  # list of primes
    num = 3
    s = 2

    while num < n:
        prime = True
        for d in p:
            if num%d == 0:
                prime = False
                break
            if d*d > num + 1:
                break
        if prime:
            p.append(num)
            s += num
        num += 2
    return s

def sum_primes_to_n(n):
    sieve = [True]*n                  # to generate list of primes
    def mark(sieve, x):               # remove sum from the return expression
        for i in xrange(x*2, n, x):
            sieve[i] = False
    for x in xrange(2, int(n**0.5)+1):
        if sieve[x]: mark(sieve, x)

    return sum(i for i in xrange(2, n) if sieve[i])

def sum_primes_better_sieve(n): # not really
    sieve = [True]*n
    def mark(sieve, x):
        for i in xrange(x*2, n, x):
            sieve[i] = False
    mark(sieve,2)
    for x in xrange(3, int(n**0.5)+1,2):
        if sieve[x]: mark(sieve, x)

    return sum(i for i in xrange(2, n) if sieve[i])

def sundaram3(max_n): # Sundaram Sieve
    ''' generates a list of primes below a number max_n.
    Note: if max_n is odd, it will generate it regardless of whether it is
    prime or not. So, always use max_n = smallest even number greater than
    or equal to max_n'''
    numbers = range(3, max_n+1, 2)
    half = (max_n)//2
    initial = 4

    for step in xrange(3, max_n+1, 2):
        for i in xrange(initial, half, step):
            numbers[i-1] = 0
        initial += 2*(step+1)

        if initial > half:
            return [2] + filter(None, numbers)

print sum_primes_better_sieve(2000000)
print sum(sundaram3(2000000))
print sum_primes_to_n(2000000)
print sum_primes_to_n_naive(2000000)
