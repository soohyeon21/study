# 14566

#
# sol1) 시간초과
#
##import sys
##
##n = int(sys.stdin.readline())
##stops = list(map(int, sys.stdin.readline().split()))
##
##dist = {}
##for i in range(n):
##    for j in range(i+1, n):
##        dist[abs(stops[i]-stops[j])] = dist.setdefault(abs(stops[i]-stops[j]), 0)
##        dist[abs(stops[i]-stops[j])] += 1
##
##min_dist = sorted(list(dist.items()), key=lambda x:x[0])[0]
##print(min_dist[0], min_dist[1])



#
# sol2) 정답
# stops를 sort하고 시작하면 for문을 2번 돌릴 필요가 없고, 시간도 단축된다.
#
import sys

n = int(sys.stdin.readline())
stops = list(map(int, sys.stdin.readline().split()))

min_dist = 32800000
min_cnt = 0
for i in range(n):
    for j in range(i+1, n):
        if (abs(stops[i]-stops[j]) < min_dist):
            min_dist = abs(stops[i]-stops[j])
            min_cnt = 1
        elif (abs(stops[i]-stops[j]) == min_dist):
            min_cnt += 1

print(min_dist, min_cnt)
