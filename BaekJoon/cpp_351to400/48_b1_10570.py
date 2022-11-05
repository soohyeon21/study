# 10570

# 1000개 원소를 갖는 list 생성해서 각 칸에 개수를 세서 넣는 방법도 있다.

import sys

n = int(sys.stdin.readline())
for _ in range(n):
    v = int(sys.stdin.readline())
    dic = {}
    for __ in range(v):
        s = int(sys.stdin.readline())
        if (s in dic):
            dic[s] += 1
        else:
            dic[s] = 1
    nlist = list(dic.items())
    nlist.sort(key=lambda x: (-x[1], x[0]))
    print(nlist[0][0])
