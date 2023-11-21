# 2750

import sys

n = int(sys.stdin.readline())
nlist = list(int(sys.stdin.readline()) for _ in range(n))

for i in range(n-1):
    for j in range(n-1-i): # -i # 이미 정렬이 완료된 끝부분은 굳이 안해도 됨.
        if (nlist[j] > nlist[j+1]):
            nlist[j], nlist[j+1] = nlist[j+1], nlist[j]

print(*nlist, sep="\n")
