# 5597

# insert(a, b) # a위치에 b값 넣기

import sys

num = [0 for x in range(30)]
num.insert(0, 1)
for _ in range(28):
    n = int(sys.stdin.readline())
    num[n] = 1

small = num.index(0)
num[small] = 1
small2 = num.index(0)
print(small)
print(small2)
