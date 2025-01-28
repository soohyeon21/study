# 24356

import sys

t1, m1, t2, m2 = map(int, sys.stdin.readline().split())

start = t1*60+m1
end = t2*60+m2
if (start > end):
    end += 24*60

total = end - start
cnt = total//30

print(total, cnt)
