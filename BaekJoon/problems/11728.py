# 11728

# while (a와 b에서 뽑은 개수가 각각 n, m을 넘지 않는지 확인하면서)

#
# sol1) 시간초과
#
##import sys
##
##n, m = map(int, sys.stdin.readline().split())
##a = list(map(int, sys.stdin.readline().split()))
##b = list(map(int, sys.stdin.readline().split()))
##
##ab = [0 for _ in range(n+m)]
##conc = a+b[::-1]
##for i in range(n+m):
##    if (conc[0] <= conc[-1]):
##        ab[i] = conc.pop(0)
##    else:
##        ab[i] = conc.pop()
##
##print(*ab)



#
# sol2) 정답
#
import sys

n, m = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))

print(*sorted(a+b))
