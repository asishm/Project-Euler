from itertools import permutations, combinations

def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n < 2:
        return False
    if n % 2 == 0:
        return False
    if n%6 != 1 and n%6 != 5:
        return False
    for k in range(3, round(n**0.5+1), 2):
        if n%k == 0:
            return False
    return True

for m in range(1000, 10000):
    if is_prime(m):
        sk = str(m)
    else:
        continue
        
    perms = [int(''.join(k)) for k in set(permutations(sk)) if k[0] != '0' and
                 k[-1] not in ('0', '2', '4', '6', '8') and
                 is_prime(int(''.join(k)))]
    choose_2 = combinations(perms, 2)

    for comb in choose_2:
        d = sorted([m, comb[0], comb[1]])
        if 2*d[1] == d[0] + d[2]:
            print(' '.join(map(str, d)))
            
