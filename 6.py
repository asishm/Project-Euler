'''Find the difference between the sum of the squares of the first one
hundred natural numbers and the square of the sum.

i.e. find (1+2+3+...+100)^2 - (1^2 + 2^2 + 3^2 + ... + 100^2)'''

# (1+2+3+...+n) = n*(n+1)/2
# (1^2 + 2^2 + 3^2 + ... + n^2) = n(n+1)(2n+1)/6
n = 100
print (n*(n+1)/2)**2 - (n*(n+1)*(2*n+1)/6)
