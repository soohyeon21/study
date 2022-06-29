# 10101

import sys

tri = []
for _ in range(3):
    tri.append(int(sys.stdin.readline()))

if (sum(tri) != 180):
    print("Error")
elif (tri.count(60) == 3):
    print("Equilateral")
elif ((tri.count(tri[0]) == 2) or (tri.count(tri[1]) == 2)):
    print("Isosceles")
else:
    print("Scalene")
