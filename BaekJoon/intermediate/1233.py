# 1233

# 덧) dictionary는 접근 속도가 faster.

import sys

s = list(map(int, sys.stdin.readline().split()))
sumlist = [0 for x in range(sum(s)+1)]

for s1 in range(1, s[0]+1):
    for s2 in range(1, s[1]+1):
        for s3 in range(1, s[2]+1):
            sumlist[s1+s2+s3] += 1
print(sumlist.index(max(sumlist)))
