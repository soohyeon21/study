# 8710

# k+m 반복은 시간 초과

#
# sol1) %1의 나머지
#
import sys

k, w, m = map(int, sys.stdin.readline().split())

cnt = (w-k)//m if ((w-k)/m%1 == 0) else (w-k)//m+1

print(cnt)



#
# sol2) math.ceil()
#
##import sys
##import math
##
##k, w, m = map(int, sys.stdin.readline().split())
##
##cnt = math.ceil((w-k)/m)
##
##print(cnt)
