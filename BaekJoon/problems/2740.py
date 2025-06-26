# 2740

# (N*M)행렬 x (M*K)행렬 = (N*K)행렬

import sys

an, am = map(int, sys.stdin.readline().split())
matrix_a = [list(map(int, sys.stdin.readline().split())) for _ in range(an)]

bm, bk = map(int, sys.stdin.readline().split())
matrix_b = [list(map(int, sys.stdin.readline().split())) for _ in range(bm)]

mmul = [[0 for x1 in range(bk)] for x2 in range(an)]

for row in range(an):
    for col in range(bk):
        for fix in range(am):
            mmul[row][col] += matrix_a[row][fix] * matrix_b[fix][col]

for line in mmul:
    print(*line)
