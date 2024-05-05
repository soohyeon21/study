# 14723

import sys

n = int(sys.stdin.readline())

before = 0
for i in range(46):
    if (i*(i+1)/2 < n <= (i+1)*(i+2)/2):
        before = i
        break

order = n - before*(before+1)//2
print(before+2-order)
print(order)
