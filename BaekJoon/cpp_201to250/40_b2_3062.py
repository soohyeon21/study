# 3062

# if (pnum == pnum[::-1]) # 아예 뒤집은 다음 비교하는 방법도 있다.

import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n = sys.stdin.readline().rstrip()
    rn = n[::-1]
    pnum = str(int(n) + int(rn))
    cnt = 0
    for i in range(len(pnum)//2): # 좌우대칭이면
        if (pnum[i] == pnum[len(pnum)-(i+1)]):
            cnt += 1
    if (cnt == len(pnum)//2):
        print("YES")
    else:
        print("NO")
