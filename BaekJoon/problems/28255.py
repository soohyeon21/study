# 28255

import sys
import math

def tail(ipt):
    return ipt[1:]

def rev(ipt):
    return ipt[::-1]

def isIce(ipt):
    sp = ipt[:math.ceil(len(ipt)/3)]

    state = False
    if (ipt == sp + rev(sp) + sp):
        state = True
    if (ipt == sp + tail(rev(sp)) + sp):
        state = True
    if (ipt == sp + rev(sp) + tail(sp)):
        state = True
    if (ipt == sp + tail(rev(sp)) + tail(sp)):
        state = True
        
    return state


t = int(sys.stdin.readline())

for _ in range(t):
    ice = sys.stdin.readline().rstrip()
    print(int(isIce(ice)))
