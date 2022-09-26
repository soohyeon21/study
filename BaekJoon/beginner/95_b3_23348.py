# 23348

# 문제 꼼꼼히 읽자~

import sys

a, b, c = map(int, sys.stdin.readline().split())
n = int(sys.stdin.readline())
club = []
for _ in range(n):
    a1, b1, c1 = map(int, sys.stdin.readline().split())
    a2, b2, c2 = map(int, sys.stdin.readline().split())
    a3, b3, c3 = map(int, sys.stdin.readline().split())
    one = a*(a1+a2+a3) + b*(b1+b2+b3) + c*(c1+c2+c3)
    club.append(one)

print(max(club))
