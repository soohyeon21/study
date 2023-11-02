# 2810

import sys

n = int(sys.stdin.readline())
man = sys.stdin.readline().rstrip().replace("LL", "L")

print(min(n, len(man)+1))
