# 6491

# 입력이 한 줄로 이루어져 있다는 보장이 없다. sys.stdin.read()를 쓰자. or while-try-except-break를 쓰든가.

# 1은 sum이 0으로 DEFICIENT이다. 주의.

import sys

nums = list(map(int, sys.stdin.read().split()))[:-1]

for num in nums:
    total = 0
    for i in range(1, num):
        if (num%i == 0):
            total += i

    if (total == num):
        print(num, "PERFECT")
    elif (total > num):
        print(num, "ABUNDANT")
    elif (total < num):
        print(num, "DEFICIENT")
