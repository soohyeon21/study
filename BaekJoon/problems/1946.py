# 1946

#
# sol1) 시간 초과
# python list slicing 시간 복잡도 = O(n)
#
##import sys
##
##t = int(sys.stdin.readline())
##for _ in range(t):
##    n = int(sys.stdin.readline())
##    cand = [tuple(map(int, sys.stdin.readline().split())) for i in range(n)]
##
##    cnt = 0
##    for k in range(n):
##        rest = cand[:k]+cand[k+1:]
##        fman = cand[k]
##        
##        state = True
##        for p in range(n-1):
##            if ((fman[0] > rest[p][0]) and (fman[1] > rest[p][1])):
##                state = False
##                break
##                
##        if (state):
##            cnt += 1
##            
##    print(cnt)



#
# sol2)
# 1) 우선 서류 성적으로 sort 하고
# 2) 면접 성적은 무조건 높아야지 선발될 수 있다.
#
import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    cand = sorted([tuple(map(int, sys.stdin.readline().split())) for i in range(n)])

    cnt = 1
    high = 0
    for i in range(1, n):
        if (cand[i][1] < cand[high][1]):
            cnt += 1
            high = i

    print(cnt)
