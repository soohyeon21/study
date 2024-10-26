# 16189

import sys

s = sys.stdin.readline().rstrip()
k = int(sys.stdin.readline())

if (s == s[::-1]):
    print("YES")
else:
    print("NO")
