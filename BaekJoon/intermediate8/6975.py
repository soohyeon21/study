# 6975

import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    
    total = 0
    for i in range(1, n):
        if (n%i == 0):
            total += i

    state = "a perfect"
    if (total < n):
        state = "a deficient"
    elif (total > n):
        state = "an abundant"

    print(f"{n} is {state} number.\n")
