# 2738

# 문제 잘 읽자.
# "둘째 줄부터 'N개'의 줄에 행렬 A의 원소 M개가 차례대로 주어진다.
# 이어서 'N개'의 줄에 행렬 B의 원소 M개가 차례대로 주어진다."

# N*M 크기의 행렬
# ( 1 ) 1, 2, ..., M
# ( 2 ) 1, 2, ..., M
# (...) 1, 2, ..., M
# ( N ) 1, 2, ..., M
# sol1에서 c 만들때 m, n 순서 주의!!

#
# sol1
#
import sys

n, m = map(int, sys.stdin.readline().split())

a = []
b = []
c = [[0 for x in range(m)] for y in range(n)]
for _ in range(n):
    a.append(list(map(int, sys.stdin.readline().split())))
for __ in range(n):
    b.append(list(map(int, sys.stdin.readline().split())))

for i in range(n):
    for j in range(m):
        c[i][j] = a[i][j] + b[i][j]

for p in range(n):
    print(*c[p])


#
# sol2
#
##import sys
##
##n, m = map(int, sys.stdin.readline().split())
##
##a = []
##b = []
##for _ in range(n):
##    a.append(list(map(int, sys.stdin.readline().split())))
##for __ in range(n):
##    b.append(list(map(int, sys.stdin.readline().split())))
##
##for i in range(n):
##    for j in range(m):
##        a[i][j] += b[i][j]
##
##for p in range(n):
##    print(*a[p])
