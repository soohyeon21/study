# 11652

# dictionary 사용도 적극 고려하자.

# dictionary => .keys(), .values(), .items()
# dictionary는 sort가 안된다. .items()+sorted() 사용하자.

import sys

n = int(sys.stdin.readline())

num = {}
for _ in range(n):
    val = int(sys.stdin.readline())
    if (val in num):
        num[val] += 1
    else:
        num[val] = 0

nlist = sorted(num.items(), key = lambda x:(-x[1], x[0]))
print(nlist[0][0])
