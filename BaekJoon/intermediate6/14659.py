# 14659

# 이중 for문은 시간초과

# greedy 문제

#
# sol1) 이건 왜 틀렸을까... append가 for 끝나고 와야한다는데...
#
##import sys
##
##n = int(sys.stdin.readline())
##bong = list(map(int, sys.stdin.readline().split()))
##
##best = []
##for i in range(n):
##    cnt = 0
##    for j in range(i+1, n):
##        if (bong[j] < bong[i]):
##            cnt += 1
##        if (bong[j] > bong[i]):
##            best.append(cnt)
##            break
##print(max(best))



#
# sol2) greedy
#
import sys

n = int(sys.stdin.readline())
bong = list(map(int, sys.stdin.readline().split()))

high = 0
best = []
cnt = 0

for val in bong:
    if (val > high):
        high = val
        cnt = 0
    else:
        cnt += 1
    best.append(cnt)

print(max(best))
