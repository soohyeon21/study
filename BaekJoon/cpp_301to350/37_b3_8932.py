# 8932

# math.floor() 대신 int()도 사용 가능한듯.

import sys
from math import floor

t = int(sys.stdin.readline())
a = [9.23076, 1.84523, 56.0211, 4.99087, 0.188807, 15.9803, 0.11193]
b = [26.7, 75, 1.5, 42.5, 210, 3.8, 254]
c = [1.835, 1.348, 1.05, 1.81, 1.41, 1.04, 1.88]
ty = ["t", "f", "f", "t", "f", "f", "t"]
for _ in range(t):
    p = list(map(int, sys.stdin.readline().split()))
    score = 0
    for i in range(7):
        if (ty[i] == "t"):
            score += floor(a[i]*(b[i]-p[i])**c[i])
        else:
            score += floor(a[i]*(p[i]-b[i])**c[i])
    print(score)
