# 10984

# print("{:.1f}" .format(3.141592)) # 3.1

import sys

t = int(sys.stdin.readline())

for _ in range(t):
    jumsu = []
    score = []
    gpa = []
    n = int(sys.stdin.readline())
    for i in range(n):
        c, g = map(float, sys.stdin.readline().split())
        jumsu.append(c)
        score.append(g)
        gpa.append(c*g)

    print("{} {:.1f}" .format(int(sum(jumsu)), (sum(gpa) / sum(jumsu))))
