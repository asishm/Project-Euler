import time

def sieve(n):
    lst = [1]*n
    lst[0], lst[1] = 0, 0
    for k in range(2*2, n, 2):
        lst[k] = 0
    div = 3
    while div <= round(n**0.5)+1:
        if lst[div]:
            for j in range(div*div, n, div):
                lst[j] = 0
        div += 2
    return lst

start = time.time()
my_sieve = sieve(1000000)
sieve_time = time.time() - start
b_vals = (i for i in range(3,1000) if my_sieve[i])

# b has to be prime since we start iterating from n = 0
# b can't be even since for n = even values, it'll be non-prime
# a can't be even since for n = 3, 9 + even + odd(b) will be even
# b has to be positive
# check if for n = 39 .. if isn't prime then we already have better candidate

max_cons = 0
max_ab = None
for b in b_vals:
    for a in range(-999, 1000, 2):
        count = 1
        val = b
        if not my_sieve[39*39 + 39*a + b]:
            continue
        for n in range(1, b):
            val += (2*n + a + 1)
            #print("val: {}, n: {}, a: {}, b: {}".format(val, n, a, b))
            if val < 0:
                break
            if my_sieve[val]:
                count += 1
            else:
                break
        if count > max_cons:
            max_cons = count
            max_ab = (a, b)
            
print(time.time() - start, sieve_time)
print(max_ab)
print(max_ab[0]*max_ab[1])
