# 25024

import sys

t = int(sys.stdin.readline())
m30 = [4, 6, 9, 11]
m31 = [1, 3, 5, 7, 8, 10, 12]
for _ in range(t):
    x, y = map(int, sys.stdin.readline().split())
    if ((0 <= x <= 23) and (0 <= y <= 59)):
        print("Yes", end=" ")
    else:
        print("No", end=" ")

    if ((x in m30) and (0 < y <= 30)):
        print("Yes")
    elif ((x in m31) and (0 < y <= 31)):
        print("Yes")
    elif ((x == 2) and (0 < y <= 29)):
        print("Yes")
    else:
        print("No")
