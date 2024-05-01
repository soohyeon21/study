# 8320

# (1, n+1), (i, n//i+1)
# or (1, n+1), (i, n+1)

#
# sol1) 시간초과
#
##import sys
##
##n = int(sys.stdin.readline())
##rect = []
##for i in range(1, n+1):
##    for j in range(1, n+1):
##        if (((i, j) not in rect) and ((j, i) not in rect) and (i*j <= n)):
##            rect.append((i, j))
##        if (i*j > n):
##            break
##
##print(len(rect))



#
# sol2)
#
import sys

n = int(sys.stdin.readline())

cnt = 0
for i in range(1, n+1):
    for j in range(i, n//i+1):
        cnt += 1

print(cnt)
