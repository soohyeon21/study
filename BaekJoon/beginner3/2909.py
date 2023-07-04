# 2909

import sys

c, k = map(int, sys.stdin.readline().split())

fore = c//10**k
rear = int((c%10**k) / 10**(k-1))
if (rear >= 5):
    fore += 1
fore *= 10**k

print(fore)
