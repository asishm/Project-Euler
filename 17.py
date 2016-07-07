'''If all the numbers from 1 to 1000 (one thousand) inclusive were written out
in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example,
342 (three hundred and forty-two) contains 23 letters and
115 (one hundred and fifteen) contains 20 letters. The use of "and"
when writing out numbers is in compliance with British usage.'''

units = {1:3, 2:3, 3:5, 4:4, 5:4, 6:3, 7:5, 8:5, 9:4, 0:0, 11:6, 12:6,
         13:8, 14:8, 15:7, 16:7, 17:9, 18:8, 19:8}
tens = {1:3, 2:6, 3:6, 4:5, 5:5, 6:5, 7:7, 8:6, 9:6}

s = 0

for n in range(1000):
    unit = n%10
    ten = (n//10)%10
    hundred = n//100
    if hundred:
        if not (ten or unit):
            s += units[hundred]+7
        elif ten and not unit:
            s += units[hundred]+7+3+tens[ten]
        elif ten < 2:
            s += units[hundred]+7+3+units[ten*10+unit]
        else:
            s += units[hundred]+7+3+tens[ten]+units[unit]
    elif ten and not unit:
        s += tens[ten]
    elif ten < 2:
        s += units[ten*10+unit]
    else:
        s += tens[ten]+units[unit]
s += 11

print(s)
