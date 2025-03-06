# 2999

# 해독하려면 암호화의 반대 과정을 거쳐야 한다.

# len(enc)+1 말고 int(n**0.5)+1 하면 easier

import sys

enc = sys.stdin.readline().rstrip()

maxR = 1
for i in range(1, len(enc)+1):
    if (len(enc)%i == 0):
        tmp_r = i
        tmp_c = len(enc)//tmp_r
        if (tmp_r <= tmp_c):
            maxR = max(maxR, tmp_r)
        else:
            break
r = maxR
c = len(enc)//r

matrix = [[0 for cl in range(c)] for rl in range(r)]

th = 0
for p in range(c):
    for q in range(r):
        matrix[q][p] = enc[th]
        th += 1

for ele in matrix:
    print(*ele, sep='', end='')
