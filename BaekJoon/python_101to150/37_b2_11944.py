# 11944

# print(n[:m]) # if-else 말고 이것도 된다.

import sys

n, m = sys.stdin.readline().split()
m = int(m)
n = n*int(n)

if (len(n) <= m):
    print(n)
else:
    print(n[:m])
