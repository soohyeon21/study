# 3273

#
# sol1) 시간 초과. 이 방법으로는 못 풀듯.
#
##import sys
##
##n = int(sys.stdin.readline())
##
##arr = sorted(list(map(int, sys.stdin.readline().split())))
##x = int(sys.stdin.readline())
##
##cnt = 0
##for val in arr:
##    if (val >= x//2): # 등호 없으면 x=12, val=6일때도 포함됨!
##        break
##    if (val < x):
##        if (x-val in arr):
##            cnt += 1
##
##print(cnt)



#
# sol2) 투 포인터 사용
# Python3, 42036KB, 100ms
#
##import sys
##
##n = int(sys.stdin.readline())
##arr = sorted(list(map(int, sys.stdin.readline().split())))
##x = int(sys.stdin.readline())
##
##left, right = 0, n-1
##cnt = 0
##while (left < right):
##    tmp = arr[left] + arr[right]
##    if (tmp == x):
##        cnt += 1
##        right -= 1 # left += 1 해도 됨
##    elif (tmp > x):
##        right -= 1
##    elif (tmp < x):
##        left += 1
##
##print(cnt)



#
# sol3) 왜 얘는 시간초과가 안되고 정답 처리될까? 이유를 모르게따...
# Python3, 202752KB, 312ms
#
##import sys
##
##n = int(sys.stdin.readline())
##arr = list(map(int, sys.stdin.readline().split()))
##x = int(sys.stdin.readline())
##
##dicta = {i:0 for i in range(2000002)}
##for val in arr:
##    dicta[val] = 1
##
##cnt = 0
##for num in arr:
##    if (num < x):
##        cnt += dicta[x-num]
##
##print(cnt//2)



#
# sol4) 오히려 sol3가 dict써서 더 빠를거라고 생각했는데, 얘가 더 빠름. 이유는 모르겠음.
# Python3, 54564KB, 136ms
#
import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
x = int(sys.stdin.readline())

nums = [0 for _ in range(2000002)]
for arr_val in arr:
    nums[arr_val] = 1

cnt = 0
for arr_val in arr:
    if (arr_val < x):
        cnt += nums[x-arr_val]

print(cnt//2)
