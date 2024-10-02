# 9288

# for문 2번
# for j in range(1, 7):
#    for k in range(j, 7):
#        if (j+k == n):
#            print(f"({j},{k})")

import sys

t = int(sys.stdin.readline())
for idx in range(1, t+1):
    n = int(sys.stdin.readline())
    
    dice = []
    for i in range(1, n//2+1):
        if ((i <= 6) and (n-i <= 6)):
            dice.append((i, n-i))

    print(f"Case {idx}:")
    for d in dice:
        print(f"({d[0]},{d[1]})")
