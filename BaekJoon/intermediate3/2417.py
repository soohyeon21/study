# 2417

# 부동소수점 오차 때문에 math.sqrt()로 해결이 안된다. 그럴거면 부동소수점 오차도 해결해줘야 함.

# 이분 탐색 사용 문제(인지는 풀이 안봤으면 몰랐을듯)
# 등호 조건 중요하다. 주의 -> 실제 제곱수 넣어봤으면 되었을듯

#
# sol1) 이분 탐색
#
##import sys
##
##n = int(sys.stdin.readline())
##
##start = 0
##end = n
##while (start <= end):
##    mid = (start + end)//2
##    if (mid**2 >= n):
##        end = mid - 1
##    else:
##        start = mid + 1
##
##print(start)



#
# sol2) math.isqrt() # 제곱근의 정수부분 반환
# 이 풀이는 제곱근의 소수 부분을 고려하지 않는 풀이이므로 부동소수점 오차와 관련이 없음.
#
import sys
import math

n = int(sys.stdin.readline())
q = math.isqrt(n)

if (q**2 < n):
    q += 1

print(q)
