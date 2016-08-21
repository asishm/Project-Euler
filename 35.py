def sieve(n):
    sieve_lst = [1]*n
    sieve_lst[1] = 0
    sieve_lst[0] = 0
    for k in range(2*2, n, 2):
        sieve_lst[k] = 0

    div = 3
    while div <= int(n**0.5)+1:
        if sieve_lst[div]:
            for k in range(div*div, n, div):
                sieve_lst[k] = 0
        div += 1
    return sieve_lst

def get_circular(n):
    lst = [str(n)]
    for k in range(1, len(str(n))):
        z = lst[k - 1]
        lst.append(z[1:]+z[0])
    return map(int, lst)

my_sieve = sieve(1000000)

print(sum(1 for k in range(1000000) if all(my_sieve[j] == 1 for j in get_circular(k))))
