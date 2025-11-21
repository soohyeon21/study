# 10855

# sort 되어 있다면 yes, 아니면 no.

import sys

n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))

if (num == sorted(num)):
    print('yes')
else:
    print('no')
