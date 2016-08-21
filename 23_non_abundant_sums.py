'''
Problem 23 (Non-abundant sums)

A perfect number is a number for which the sum of its proper divisors is
exactly equal to the number. For example, the sum of the proper divisors of 28
would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less
than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest
number that can be written as the sum of two abundant numbers is 24.
By mathematical analysis, it can be shown that all integers greater than 28123
can be written as the sum of two abundant numbers. However, this upper limit
cannot be reduced any further by analysis even though it is known that the
greatest number that cannot be expressed as the sum of two abundant
numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of
two abundant numbers.
'''

def divisors(n):
    result = set((1,))
    for i in range(2, round(n**.5)+1):
        if n%i == 0:
            result.add(i)
            result.add(n//i)
    return result

def gen_abundant(limit):
    i = 1
    while i <= limit:
        if sum(divisors(i)) > i:
            yield i
        i += 1

if __name__ == "__main__":
    import time
    start = time.time()
    abuns = tuple(gen_abundant(28123+1))
    alen = len(abuns)
    abun_sieve = [False]*28124
    for i,k in enumerate(abuns):
        for j in range(i, alen):
            cur_s = k + abuns[j]
            if cur_s > 28123:
                break
            abun_sieve[cur_s] = cur_s

    print(28123*28124/2 - sum(abun_sieve))
    print(time.time() - start)
