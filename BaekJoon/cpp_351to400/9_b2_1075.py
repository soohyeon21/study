# 1075

import sys

n = int(sys.stdin.readline())
f = int(sys.stdin.readline())

left = n%f
last2 = int(str(n)[-2:])
if (last2 - left < 0):
    n += (f-left)
else:
    n -= left
last2 = int(str(n)[-2:])

out = 0
for i in range(1, 100):
    if (last2 - f*i < 0):
        out = i-1
        break
n -= out*f

rst = str(n)[-2:]
print(rst)
