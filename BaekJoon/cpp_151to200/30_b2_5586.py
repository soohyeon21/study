# 5586

import sys

s = sys.stdin.readline().rstrip()
j = "JOI"
i = "IOI"
cntj = 0
cnti = 0

for k in range(len(s) - 2):
    if (s[k:k+3] == j):
        cntj += 1
    elif (s[k:k+3] == i):
        cnti += 1

print(cntj)
print(cnti)
