# 28097

import sys

n = int(sys.stdin.readline())
study = list(map(int, sys.stdin.readline().split()))

totalh = sum(study)+8*(len(study)-1)

print(totalh//24, totalh%24)
