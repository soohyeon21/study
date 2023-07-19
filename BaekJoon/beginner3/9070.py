# 9070

# 실수!ㅋㅋㅋㅋ

import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    mat = []
    for i in range(n):
        w, c = map(int, sys.stdin.readline().split())
        per = w/c
        mat.append((w, c, per))
    order = sorted(mat, key=lambda x:(-x[2], x[1]))
    print(order[0][1])
