# 17213

# math.comb() or math.factorial()

import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

fact = [1, 1, 2]
for i in range(3, 30):
    fact.append(fact[i-1]*i)

print(fact[m-1]//(fact[n-1]*fact[m-n]))
