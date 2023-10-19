# 2435

#
# sol1) new_temperature 구하고 max(list) 하기
#
##import sys
##
##n, k = map(int, sys.stdin.readline().split())
##temp = list(map(int, sys.stdin.readline().split()))
##
##newt = [sum(temp[i:i+k]) for i in range(n-k+1)]
##
##print(max(newt))



#
# sol2) 한번에 max값 구하기
#
import sys

n, k = map(int, sys.stdin.readline().split())
temp = list(map(int, sys.stdin.readline().split()))

maxnewt = max(sum(temp[i:i+k]) for i in range(n-k+1))

print(maxnewt)
