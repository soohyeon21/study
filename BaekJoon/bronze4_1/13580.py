# 13580

import sys

def canBack(nlist):
    if (len(set(nlist)) <= 2):
        return True
    for i in nlist:
        if (sum(nlist) == i*2):
            return True
    
    return False


num = list(map(int, sys.stdin.readline().split()))

state = canBack(num)
if (state):
    print("S")
else:
    print("N")
