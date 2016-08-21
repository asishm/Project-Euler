'''Find the largest palindrome made from the product of two 3-digit numbers.'''

def is_palindrome(n):
    return str(n) == str(n)[::-1]

print(max((i*j, i, j) for i in range(100,1000) for j in range(100,1000) if
           is_palindrome(i*j)))
