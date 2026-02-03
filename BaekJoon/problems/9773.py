# 9773

import sys

n = int(sys.stdin.readline())

for _ in range(n):
    num = sys.stdin.readline().rstrip()
    result = sum(int(digit) for digit in num) + int(num[-3:])*10
    if (result >= 1000):
        result = int(str(result)[-4:])
    else:
        result += 1000

    print(f"{result:04d}")
