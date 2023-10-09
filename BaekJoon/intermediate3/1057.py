# 1057

# 쳇

#
# sol1) math 모듈 사용
#
##import sys
##import math
##
##n, kim, lim = map(int, sys.stdin.readline().split())
##
##for i in range(1, math.ceil(math.log(n, 2))+2):
##    if (kim == lim):
##        print(i-1)
##        break
##    else:
##        kim = math.ceil(kim/2)
##        lim = math.ceil(lim/2)
##    #print(i, kim, lim)



#
# sol2) 같은 흐름 but math 모듈 사용X
#
import sys

n, kim, lim = map(int, sys.stdin.readline().split())

cnt = 0
while (kim != lim):
    kim -= kim//2
    lim -= lim//2
    cnt += 1

print(cnt)
