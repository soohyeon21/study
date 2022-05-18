# 11586

import sys

n = int(sys.stdin.readline())

mirror = []
for _ in range(n):
    mirror.append(sys.stdin.readline().rstrip())

psy = int(sys.stdin.readline())
if (psy == 1): # 있는 그대로
    for i in range(n):
        print(mirror[i])
elif (psy == 2): # 좌/우 반전
    for j in range(n):
        print(mirror[j][::-1])
elif (psy == 3): # 상/하 반전
    for k in range(n):
        print(mirror[(n-1)-k])
