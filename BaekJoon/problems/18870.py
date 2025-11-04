# 18870

import sys

n = int(sys.stdin.readline())
xn = list(map(int, sys.stdin.readline().split()))
s_xn = sorted(list(set(xn)))

xn_dict = {s_xn[i]:i for i in range(len(s_xn))}

for each in xn:
    print(xn_dict[each], end=' ')
