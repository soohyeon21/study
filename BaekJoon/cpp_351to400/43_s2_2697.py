# 2697

# test case: 634, 232, 132

# 흐헷 틀리고 나서 풀이 안보고 수정했는데, 맞췄다~

import sys

t = int(sys.stdin.readline())
for _ in range(t):
    num = sys.stdin.readline().rstrip()
    now = [int(num[x]) for x in range(len(num))]

    rst = []
    state = False
    for i in range(-1, -len(num), -1):
        if (now[i] > now[i-1]):
            piv = now[i-1]
            tmp = sorted(now[i-1:])
            for j in range(len(tmp)):
                if (tmp[j] > piv):
                    nxt = tmp.pop(j)
                    break
            rst = now[:i-1] + [nxt] + sorted(tmp)
            state = True
            break
        else:
            state = False
    if (state):
        print(*rst, sep="")
    else:
        print("BIGGEST")
