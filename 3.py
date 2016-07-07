'''What is the largest prime factor of the number 600851475143 ?'''

n = 600851475143


def largest_prime_factor(n):
    n_copy = n          # copy of the initial number
    p = None            # initialize largest prime to None
    if n%2 == 0:        # check for divisibility with 2 and repeatedly divide
        p = 2
        while n%2 == 0:
            n /= 2
    divisor = 3         # initialize divisor to 3
    while divisor**2 <= n_copy and n > 1:    # loop while n exists upto n**0.5
        if n%divisor == 0:
            p = divisor
            while n%divisor == 0:
                n /= divisor
        divisor += 2
    return p if p else n_copy     # p = None implies it is prime
print(largest_prime_factor(n))

