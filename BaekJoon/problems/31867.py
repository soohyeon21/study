# 31867

import sys

n = int(sys.stdin.readline())
k = sys.stdin.readline().rstrip()

even = 0
odd = 0
for digit in k:
    if (int(digit)%2 == 0):
        even += 1
    else:
        odd += 1

if (even > odd):
    print(0)
elif (even < odd):
    print(1)
else:
    print(-1)
