# 28353

# cf) k=10, wn=[3,4,5,6,7,9]인 경우

#
# sol1) 틀림. 반례가 뭐가 있을까?
#
##import sys
##
##n, k = map(int, sys.stdin.readline().split())
##wn = sorted(list(map(int, sys.stdin.readline().split())))
##
##happy = 0
##for i in range(-1, -n, -1):
##    if (wn[0]+wn[i] <= k):
##        for j in range((n+i+1)//2):
##            if (wn[j]+wn[n+i-j] <= k):
##                happy += 1
##        break
##
##print(happy)



#
# sol2) 투 포인터 방식. 
#
import sys

n, k = map(int, sys.stdin.readline().split())
wn = sorted(list(map(int, sys.stdin.readline().split())))

start = 0
end = n-1
happy = 0
while (start < end):
    if (wn[start]+wn[end] <= k):
        happy += 1
        start += 1
    end -= 1

print(happy)
