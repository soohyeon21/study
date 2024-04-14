# 15652

#
# sol1) Python 시간초과, PyPy3 정답
#
##import sys
##
##def dfs():
##    if (len(s) == m):
##        for k in range(m-1):
##            if (s[k] > s[k+1]):
##                return
##        print(*s)
##        return
##
##    for i in range(1, n+1):
##        s.append(i)
##        dfs()
##        s.pop()
##
##n, m = map(int, sys.stdin.readline().split())
##s = []
##dfs()



#
# sol2) dfs()에 parameter 넣기
#
import sys

def dfs(x):
    if (len(s) == m):
        print(*s)
        return

    for i in range(x, n+1): # 파라미터로 받은 숫자보다 같거나 커야 함.
        s.append(i)
        dfs(i)
        s.pop()

n, m = map(int, sys.stdin.readline().split())
s = []
dfs(1)
