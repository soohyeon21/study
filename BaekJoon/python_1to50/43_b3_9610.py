# 9610

# 허. 제일 마지막에 axis 말고 2를 써놔서 틀렸다. 어이없음.

import sys

n = int(input())

q1, q2, q3, q4, axis = 0, 0, 0, 0, 0

for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    if ((0 < x) and (0 < y)):
        q1 += 1
    elif ((0 > x) and (0 < y)):
        q2 += 1
    elif ((x < 0) and (y < 0)):
        q3 += 1
    elif ((x > 0) and (y < 0)):
        q4 += 1
    else:
        axis += 1
print("Q1: %d" %q1)
print("Q2: {}" .format(q2))
print("Q3: %d" %(q3))
print("Q4: {0}" .format(q4))
print("AXIS:", axis)
