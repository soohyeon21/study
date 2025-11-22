# 1440

#
# sol1) 일일이 모든 경우를 확인하는 경우.
#
##import sys
##
##t = list(map(int, sys.stdin.readline().split(":")))
##
##poss = [[], [], []]
##for i in range(3):
##    if (1 <= t[i] <= 12):
##        poss[i].append(1) # hour
##    if (0 <= t[i] <= 59):
##        poss[i].append(2) # minute
##    if (0 <= t[i] <= 59):
##        poss[i].append(3) # second
##
##caset = set()
##for k in range(6):
##    rst = [0, 0, 0]
##    for p1 in range(len(poss[0])):
##        rst[0] = poss[0][p1]
##        for p2 in range(len(poss[1])):
##            if (poss[1][p2] not in rst):
##                rst[1] = poss[1][p2]
##            for p3 in range(len(poss[2])):
##                if (poss[2][p3] not in rst):
##                    rst[2] = poss[2][p3]
##                if (rst.count(0) == 0):
##                    caset.add(''.join(map(str, rst)))
##                    rst[2] = 0
##            if (rst.count(0) == 1):
##                rst[1], rst[2] = 0, 0
##        if (rst.count(0) == 2):
##            rst[0] = 0
##            
##print(len(caset))



#
# sol2) hour만 전체 가능 개수에 영향을 끼침 + 제대로인 된 시간인지 확
#
import sys

t = list(map(int, sys.stdin.readline().split(":")))

h = 0
right = True
for i in range(3):
    if (1 <= t[i] <= 12):
        h += 1 # hour
    if (t[i] > 59):
        right = False
        
print(2*h*int(right))
