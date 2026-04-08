# 31616

import sys

n = int(sys.stdin.readline())
s = sys.stdin.readline().rstrip()

if (len(set(s)) == 1):
    print("Yes")
else:
    print("No")
