# 16020

# 1)
# 1 2 3
# 3 5 7
# 4 6 9

# 2)
# 3 7 9
# 2 5 6
# 1 3 4

# 3)
# 9 6 4
# 7 5 3
# 3 2 1

# 4)
# 4 3 1
# 6 5 2
# 9 7 3

import sys

n = int(sys.stdin.readline())
data = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# 1) 그대로
if ((data[0][0] < data[0][1]) and (data[0][0] < data[1][0])):
    for one in data:
        print(*one)
        
# 2) 우회전x1 필요
elif ((data[0][0] < data[0][1]) and (data[0][0] > data[1][0])):
    for i in range(n):
        for j in range(-1, -n-1, -1):
            print(data[j][i], end=" ")
        print()

# 3) 우회전x2 필요
elif ((data[0][0] > data[0][1]) and (data[0][0] > data[1][0])):
    for k in range(-1, -n-1, -1):
        print(*data[k][::-1])

# 4) 우회전x3 필요
else:
    for p in range(-1, -n-1, -1):
        for q in range(n):
            print(data[q][p], end=" ")
        print()
