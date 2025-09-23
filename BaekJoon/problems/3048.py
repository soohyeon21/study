# 3048

# 첫번째 그룹의 각 개미의 idx를 확인해서, 만약에 해당 (idx+1)에 두번째 그룹의 개미가 있다면 swap.

import sys

n1, n2 = map(int, sys.stdin.readline().split())
ant1 = list(sys.stdin.readline().rstrip())
ant2 = list(sys.stdin.readline().rstrip())
t = int(sys.stdin.readline())

road = ant1[::-1] + ant2

forward = [i for i in range(n1)]
check = [-1] + forward + [n1+n2]
for sec in range(t):
    new_forward = []
    for one in forward:
        if (one+1 not in check):
            road[one], road[one+1] = road[one+1], road[one]
            new_forward.append(one+1)
        else:
            new_forward.append(one)
    forward = new_forward
    check = [-1]+forward+[n1+n2]

print(''.join(road))
