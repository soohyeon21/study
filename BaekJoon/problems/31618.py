# 31618

# list에서 (값 in list) # O(n)
# set에서 (값 in set) # O(1) # set은 해시 테이블 기반.

import sys

n = int(sys.stdin.readline())
an = set(map(int, sys.stdin.readline().split()))

state = False
for num in an:
    if ((num+3 in an) and (num+6 in an)):
        state = True
        break

if (state):
    print("Yes")
else:
    print("No")
