# 17588

#
# sol1) dictionary 사용
#
##import sys
##
##n = int(sys.stdin.readline())
##nlist = [int(sys.stdin.readline()) for _ in range(n)]
##ndict = {x:0 for x in range(1, nlist[-1]+1)}
##for num in nlist:
##    ndict[num] = 1
##
##state = True
##for key, value in ndict.items():
##    if (value == 0):
##        state = False
##        print(key)
##
##if (state):
##    print("good job")



#
# sol2) 세 달전 풀이 조금 손 봄.
#
import sys

times = int(sys.stdin.readline())
num = [False for i in range(201)]
last = 0
for _ in range(times):
    n = sys.stdin.readline().rstrip()
    last = int(n)
    num[int(n)] = True

cnt = 0
for k in range(1, last+1):
    if (not num[k]):
        cnt = 1
        print(k)
if (not cnt):
    print("good job")
