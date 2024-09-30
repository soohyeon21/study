# 7489

# n! # math.factorial(n)

import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    
    fact = 1
    for i in range(1, n+1):
        fact *= i
        
    for k in str(fact)[::-1]:
        if (k != "0"):
            print(k)
            break
