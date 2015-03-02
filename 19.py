''' 1 Jan 1900 was a Monday.

How many Sundays fell on the first of the month during the twentieth century
(1 Jan 1901 to 31 Dec 2000)?'''

import datetime

start = 1901
end = 2000

count  = 0
for y in xrange(start, end+1):
    for m in xrange(1,13):
        if datetime.date(y,m,1).weekday() == 6:
            count += 1
print count
