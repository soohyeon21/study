# 3182

import sys

n = int(sys.stdin.readline())

seni = {i:0 for i in range(1, n+1)}
for _ in range(n):
    ask = int(sys.stdin.readline())
    seni[ask] += 1

sort_seni = sorted(list(seni.items()), key=lambda x:(x[1], x[0]))
print(sort_seni[0][0])
