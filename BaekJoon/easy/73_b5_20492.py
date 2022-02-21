# 20492

# c2 구할 때, (1-n*0.2*0.22) 해도 된다.

import sys

n = int(sys.stdin.readline())
c1 = int(n * 0.78)
c2 = int(n * 0.8 + (n * 0.2 * 0.78))
print(c1, c2)
