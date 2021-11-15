# 1292

# 헛참... 간단한 풀이로군...

# slicing으로 범위 제한해서 sum()도 가능함.

import sys

a, b = map(int, sys.stdin.readline().split())
arr = []

for i in range(1, 46):
    arr += [i] * i
print(sum(arr[a-1:b]))





# 틀린 풀이. (40, 46)을 넣으면 답이 다르다.
#
##import math
##import sys
##
##def easy(cnt):
##    num = math.floor((math.sqrt(4*cnt) - 1) / 2) + 1
##    th = (num**2 + num) // 2
##    sigma = (num * (num + 1) * (2*num + 1)) // 6
##    more = (cnt - th) * (num + 1)
##    #print(cnt, num, th, sigma, more)
##    sigma += more
##    return sigma
##
##a, b = map(int, sys.stdin.readline().split())
##
##print(easy(b) - easy(a-1))
