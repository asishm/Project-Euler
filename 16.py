'''What is the sum of the digits of the number 2^1000?'''

print sum(map(int, str(2**1000)))

# pretty cute
# assume python couldn't handle big numbers

# number of digits in 2**1000 ~ 1000*log(2) base 10 ~ 300

from math import log

def calculate(base=2, POW=1000):

    digits = int(POW*log(base,10))+20
    value = [0]*digits            # ^ to be safe
    value[0] = 1

    power = 0
    index = 1  # stores the smallest index of value which is currently 0


    while power < POW:
        carry = 0
        for j in xrange(index):
            value[j] = value[j]*base + carry
            carry = value[j]/10
            value[j] %= 10
        if carry:
            value[index] = carry
            index += 1
        #print ''.join(str(_) for _ in value[:index][::-1]),
        power += 1
    return value, index

print sum(calculate()[0])
# to print 2**1000
# val, ind = calculate(2,1000)
# print ''.join(str(_) for _ in val[:ind][::-1])
