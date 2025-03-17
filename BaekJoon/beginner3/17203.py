# 17203

# 변화량 list, 누적합 list, 단순 value[end]-value[start] 사용하면 시간 1/10 수준으로 대폭 단축 가능.

# 부분 배열 합: O(N)
# 누적합: O(1)

# 
# sol1) 매번 델타 구하기
# 32412 KB, 316 ms
#
##import sys
##
##n, q = map(int, sys.stdin.readline().split())
##an = list(map(int, sys.stdin.readline().split()))
##
##for _ in range(q):
##    start, end = map(int, sys.stdin.readline().split())
##    delta = 0
##    for i in range(start-1, end-1):
##        delta += abs(an[i]-an[i+1])
##    print(delta)



#
# sol2) 누적합 구하기
# 32412 KB, 36 ms
#
import sys

n, m = map(int, sys.stdin.readline().split())
an = list(map(int, sys.stdin.readline().split()))

diff_cum = [0 for i in range(n)]
for j in range(1, n):
    diff_cum[j] = diff_cum[j-1] + abs(an[j]-an[j-1])

for _ in range(m):
    start, end = map(int, sys.stdin.readline().split())
    print(diff_cum[end-1] - diff_cum[start-1])
