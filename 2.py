'''By considering the terms in the Fibonacci sequence whose values do not
exceed four million, find the sum of the even-valued terms.'''

a,b = 1,1  # first two fib numbers
s = 0      # required sum
while max(a,b)<=4*1E6:   # constraint
    b,a=a+b,b            # generate next fib number (b)
    if b%2==0:
        s += b
print s

