# 10834

import sys

def gcf(a, b):
    while (b != 0):
        num = a%b
        a = b
        b = num
    return a

def lcm(a, b):
    return a*b//gcf(a, b)


m = int(sys.stdin.readline())
pair = {i:tuple(map(int, sys.stdin.readline().split())) for i in range(1, m+1)}

clock = pair[1][2]
turn = [clock, clock]
ratio = [pair[1][0], pair[1][1]]

for k in range(2, m+1):
    pre = lcm(ratio[-1], pair[k][0])//ratio[-1]
    pro = lcm(ratio[-1], pair[k][0])//pair[k][0]
    for p in range(k):
        ratio[p] *= pre
    ratio.append(pro*pair[k][1])
    clock = (clock+pair[k][2])%2
    turn.append(clock)

print(turn[-1], ratio[-1]//ratio[0])
