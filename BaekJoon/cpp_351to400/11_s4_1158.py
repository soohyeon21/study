# 1158

# 굳이 while(1) 안써도 됐다. (n-1)번만 실행해도 되었을 것을.

import sys

n, k = map(int, sys.stdin.readline().split())
num = [x for x in range(1, n+1)]

loc = k-1
rst = []
while (1):
    if (len(num) == 1):
        break

    value = num.pop(loc)
    rst.append(value)
    loc = (loc+(k-1))%len(num)
rst.append(num[0])

print("<", end="")
print(*rst, sep=", ", end="")
print(">")
