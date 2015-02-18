'''What is the 10,001st prime number?'''

def get_nth_prime(n):
    primes = [2]
    if n == 1: return 2
    length = 1
    num = 3
    while length <= n:
        for prime in primes:
            if prime**2 > num:
                length += 1
                primes.append(num)
                break
            if num%prime == 0:
                break
        num += 2
    return primes[n-1]

