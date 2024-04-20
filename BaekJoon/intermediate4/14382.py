# 14382

import sys

t = int(sys.stdin.readline())
for idx in range(1, t+1):
    n = int(sys.stdin.readline())
    digit = [False for x in range(10)]
    
    if (n == 0):
        print(f"Case #{idx}: INSOMNIA")
        continue

    times = 1
    while (1):
        for letter in str(n*times):
            digit[int(letter)] = True

        if (False not in digit):
            print(f"Case #{idx}: {n*times}")
            break
        times += 1
