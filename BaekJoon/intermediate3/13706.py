# 13706

# 이분 탐색

#
# sol1) 이분 탐색1
# mid = (start+end)//2를 따로 뺄 수 있겠다.
# mid 기준 +- 1 하는게 더 나을듯.
#
##import sys
##
##n = int(sys.stdin.readline())
##
##start = 1
##end = 10**800 - 1
##mid = (start+end)//2
##while (start <= end):
##    if (mid**2 == n):
##        break
##
##    if (mid**2 > n):
##        end = mid
##    elif (mid**2 < n):
##        start = mid
##    mid = (start+end)//2
##
##print(mid)



#
# sol2) 이분 탐색2
#
import sys

n = int(sys.stdin.readline())

start = 1
end = n
while (start <= end): # while (1): 도 가능
    mid = (start+end)//2
    if (mid**2 == n):
        print(mid)
        break
    elif (mid**2 > n):
        end = mid - 1
    elif (mid**2 < n):
        start = mid + 1
