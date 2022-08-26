# 3059

import sys

t = int(sys.stdin.readline())
for _ in range(t):
    asc = sys.stdin.readline().rstrip()
    val = 0

    for num in range(65, 91):
        if (chr(num) not in asc):
            val += num
    print(val)
