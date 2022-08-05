# 1568

# 와 시간초과 뜰 줄 알았는데ㅎ

import sys

n = int(sys.stdin.readline())

bird = 0
sec = 0
now = 1
while (bird != n):
    if (now > n-bird):
        now = 1
    else:
        bird += now
        sec += 1
        now += 1
print(sec)
