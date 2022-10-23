# 10163

# 마지막 조건은 1001x1001 크기의 격자판

# list a에 대해 'a[:3] = [22]*3' 하면 a[:3]이 22로 대체됨.

#
# 맞는 풀이 1)
# python3로 하면 시간초과
# pypy3로 하면 시간초과 안뜸
#
##import sys
##
##n = int(sys.stdin.readline())
##paper = [[0 for aa in range(1001)] for bb in range(1001)]
##for i in range(1, n+1):
##    x, y, w, h = map(int, sys.stdin.readline().split())
##    for height in range(h):
##        for width in range(w):
##            paper[y+height][x+width] = i
##
##nsum = [0 for cc in range(n)]
##for k in range(1001):
##    for idx in range(1, n+1):
##        nsum[idx-1] += paper[k].count(idx)
##
##print(*nsum, sep="\n")


#
# 맞는 풀이 2)
# python3로 100점!
#
import sys

n = int(sys.stdin.readline())
paper = [[0 for aa in range(1001)] for bb in range(1001)]
for i in range(1, n+1):
    x, y, w, h = map(int, sys.stdin.readline().split())
    for height in range(h):
        paper[y+height][x:x+w] = [i]*w # 이 부분 변화

nsum = [0 for cc in range(n)]
for k in range(1001):
    for idx in range(1, n+1):
        nsum[idx-1] += paper[k].count(idx)

print(*nsum, sep="\n")
