# 1964

import sys

n = int(sys.stdin.readline())

dots = n*(n+1)//2*3 + n+1
rmd = dots % 45678

print(rmd)
