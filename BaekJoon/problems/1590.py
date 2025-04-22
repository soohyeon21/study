# 1590

import sys

n, t = map(int, sys.stdin.readline().split())

result = []
for _ in range(n):
    s, l, c = map(int, sys.stdin.readline().split())
    bus += [s+i*l for i in range(c)]

    if (bus[-1] < t):
        continue

    bus.sort()
    wait = 0

    if (bus[-1] < t):
        wait = -1
    else:
        left = 0
        right = len(bus)-1
        answer = 0
        while (left <= right):
            #print(f"left={left}, right={right}")
            mid = (left+right)//2
            if (bus[mid] < t):
                answer = mid
                left = mid + 1
            else:
                right = mid - 1
            
            
##        if (t < bus[(left+right)//2]):
##            right = (left+right)//2
##        elif (t > bus[(left+right)//2]):
##            left = (left+right)//2
##        elif (t == bus[(left+right)//2]):
##            break
##
##        if (abs(left-right) == 1):
##            break
        
    wait = min(abs(bus[left]-t), abs(t-bus[right]))
##    print(bus)
##    print(left, right)
print(wait)
