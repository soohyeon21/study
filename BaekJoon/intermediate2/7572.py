# 7572

import sys

n = int(sys.stdin.readline())
n12 = ["I", "J", "K", 'L', 'A', 'B', "C", 'D', 'E', 'F', 'G', 'H']
n10 = [6, 7, 8, 9, 0, 1, 2, 3, 4, 5]

western = n12[n%12]+str(n10[n%10])
print(western)
