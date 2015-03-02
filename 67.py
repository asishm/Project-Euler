'''Find the maximum total from top to bottom in triangle.txt
a 15K text file containing a triangle with one-hundred rows.'''

import os.path
with open(os.path.join(os.path.abspath(''),'files/p067_triangle.txt'), 'r') as f:
    r = f.read().strip().split('\n')

M = [map(int, c.split()) for c in r]
N = [map(int, c.split()) for c in r][::-1]

# top -> bottom
for i,c in enumerate(M):
    if i == 0:
        continue
    for j in xrange(len(c)):
        if j == 0:
            M[i][j] += M[i-1][j]
        elif j == len(c)-1:
            M[i][j] += M[i-1][j-1]
        else:
            M[i][j] += max(M[i-1][j], M[i-1][j-1])
print max(M[-1])

# bottom -> top

for i,c in enumerate(N):
    if i == 0:
        continue
    for j in xrange(len(c)):
        N[i][j] += max(N[i-1][j], N[i-1][j+1])
print N[-1][0]
            
