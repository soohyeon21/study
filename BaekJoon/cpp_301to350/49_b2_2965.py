# 2965

# ((a==b) and (b==c))에 not을 붙이면 ((a!=b) or (b!=c))

import sys

kan = list(map(int, sys.stdin.readline().split()))
cnt = 0

while ((kan[2] != kan[1]+1) or (kan[1] != kan[0]+1)):
    if (kan[2]-kan[1] >= kan[1]-kan[0]):
        kan[0] = kan[2]-1
    else:
        kan[2] = kan[0]+1
    kan.sort()
    cnt += 1
print(cnt)
