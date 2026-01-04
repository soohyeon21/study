# 34750

import sys

n = int(sys.stdin.readline())

parents = 0
if (n >= 1000000):
    parents = n*0.2
elif (n >= 500000):
    parents = n*0.15
elif (n >= 100000):
    parents = n*0.1
else:
    parents = n*0.05

print(int(parents), int(n-parents))
