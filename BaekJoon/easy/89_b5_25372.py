# 25372

import sys

n = int(sys.stdin.readline())
for _ in range(n):
    pw = sys.stdin.readline().rstrip()
    if (6 <= len(pw) <= 9):
        print("yes")
    else:
        print("no")
