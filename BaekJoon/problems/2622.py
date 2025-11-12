# 2622

# or, 가장 긴 변이 가질 수 있는 범위를 계산해서, 그에 따른 나머지 변의 길이의 가능 조합을 찾는 방법도 있다.

#
# sol1) python3 시간초과, pypy3 메모리 초과
#
##import sys
##
##n = int(sys.stdin.readline())
##
##poss = set()
##for t1 in range(1, n-1):
##    for t2 in range(t1, n):
##        if (max(t1, t2, n-(t1+t2)) < n-max(t1, t2, n-(t1+t2))):
##            poss.add(tuple(sorted([t1, t2, n-(t1+t2)])))
##
##print(len(poss))



#
# sol2) python3, pypy3 시간초과
#
##import sys
##
##def isTriangle(edge):
##    t1, t2, t3 = edge[0]-1, edge[1], edge[2]
##    possible = []
##    for d1, d2 in [(1, 0), (0, 1)]:
##        if (max(t2+d1, t3+d2) < t1+min(t2+d1, t3+d2)):
##            pair = (t1, min(t2+d1, t3+d2), max(t2+d1, t3+d2))
##            if (pair not in possible):
##                possible.append(pair)
##    return possible
##
##
##n = int(sys.stdin.readline())
##
##triangle = [0, 0, 0, 1, 0, 1, 1, 2]
##cnt = 0
##if (n <= 7):
##    cnt = triangle[n]
##else:
##    edges = {n//3:[(n//3, n//3, n//3+n%3)]}
##    for min_edge in reversed(range(2, n//3+1)):
##        for edge in edges[min_edge]:
##            smaller = isTriangle(edge)
##            
##            edges[min_edge-1] = edges.setdefault(min_edge-1, [])
##            for small in smaller:
##                if (small not in edges[min_edge-1]):
##                    edges[min_edge-1].append(small)
##    cnt = sum(len(value) for value in edges.values())
##
##print(cnt)



#
# sol3) python3 시간초과, pypy3 정답
#
import sys

n = int(sys.stdin.readline())

cnt = 0
for t1 in range(1, n-1):
    for t2 in range(t1, n):
        t3 = n - (t1+t2)
        if (t3 < t2): # t1 <= t2 <= t3
            break
        else:
            if (t3 < t1+t2):
                cnt += 1

print(cnt)
