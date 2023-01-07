# 10974

#
# sol1) DFS
#
import sys

def dfs():
    if (len(tmp) == n):
        print(*tmp)
        return
    for i in range(1, n+1):
        if (i not in tmp):
            tmp.append(i)
            dfs()
            tmp.pop()    

n = int(sys.stdin.readline())
tmp = []

dfs()


#
# sol2) permutation
#
##import sys
##from itertools import permutations
##
##n = int(sys.stdin.readline())
##num = [x for x in range(1, n+1)]
##per = permutations(num, n)
##for p in per:
##    print(*p)
