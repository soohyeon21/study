# 3595

# 방법1) a, b, c가 가장 비슷하면 될듯 한데, 그 이후로는 모르겠음.
# 방법2) 브루트포스 문제 - (a, b, c)의 범위를 제한해주면 더 좋을듯 (n의 인수가 되도록)

import sys

n = int(sys.stdin.readline())

surface = 10**12
answer = ()
#for a in range(1, n+1): # Python3: 2232ms
for a in range(1, int((n+1)**0.5)+1): # Python3: 1108ms
    for b in range(1, n//a+1):
        if (n%(a*b) == 0):
            c = n//(a*b)
            if ((a*c+b*c+a*b)*2 < surface):
                answer = (a, b, c)
                surface = (a*c+b*c+a*b)*2

print(*answer)
