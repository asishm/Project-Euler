'''Find the sum of all the multiples of 3 or 5 below 1000.'''

L = [0]*1000

for i,c in enumerate(L):
    if i%3 == 0 or i%5 == 0:
        L[i] = i
print(sum(L))

# Alternatively

print(sum(c for c in range(1000) if c%3 == 0 or c%5 == 0))
