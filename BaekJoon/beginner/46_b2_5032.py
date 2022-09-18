# 5032

# 흠. 사람 생각은 다 비슷비슷한가 보군.

import sys

e, f, c = map(int, sys.stdin.readline().split())
cnt = 0
rmd = e+f

while (rmd >= c):
    cnt += rmd//c
    rmd = rmd%c + rmd//c

print(cnt)
