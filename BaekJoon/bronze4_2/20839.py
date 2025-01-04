# 20839

# 성적 기준(x, y, x)과 학생 점수(a, b, c)가 주어질 때
# A : 3과목 모두 기준 충족
# B : x 기준의 절반 점수 이상, 나머지는 기준 충족
# C : y, z 기준 충족
# D : y 기준의 절반 점수 이상, z는 충족
# E : z 기준 충족

import sys

x, y, z = map(int, sys.stdin.readline().split())
a, b, c = map(int, sys.stdin.readline().split())

if ((a >= x) and (b >= y) and (c >= z)):
    print("A")
elif ((a >= x/2) and (b >= y) and (c >= z)):
    print("B")
elif ((b >= y) and (c >= z)):
    print("C")
elif ((b >= y/2) and (c >= z)):
    print("D")
elif (c >= z):
    print("E")
