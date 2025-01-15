# 27961

#
# sol1) 단순 2배, 이상되면 stop
#
##import sys
##
##n = int(sys.stdin.readline())
##
##cnt = 1
##now = 1
##while (1):
##    now *= 2
##    cnt += 1
##    if (now >= n):
##        break
##
##if (n == 0):
##    print(0)
##elif (n == 1):
##    print(1)
##else:
##    print(cnt)



#
# sol2) min 사용, 이상되면 stop
# 만약 now=1, n=0이면 무한루프 발생. 그래서 시간초과 떴나 봄.
#
import sys

n = int(sys.stdin.readline())

cnt = 1
now = 1
while (1):
    if (now < n):
        now = min(n, now*2)
        cnt += 1
    if (now >= n): # '>'없으면 시간초과
        break

if (n == 0):
    print(0)
elif (n == 1):
    print(1)
else:
    print(cnt)
