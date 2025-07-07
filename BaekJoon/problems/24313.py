# 24313

# (a1*n0+a0 <= c*n0) and (c-a1>=0) # 이렇게만 해도 충분
# (c-a1<0)이면 '모든 n>=n0'에 대해서 성립이 안된다.

import sys

a1, a0 = map(int, sys.stdin.readline().split())
c = int(sys.stdin.readline())
n0 = int(sys.stdin.readline())

state = True
if ((c-a1) > 0):
    if (a0/(c-a1) > n0):
        state = False
elif ((c-a1) < 0):
    state = False
elif (c == a1):
    if (a0 > 0):
        state = False

if (state):
    print(1)
else:
    print(0)
