# 14547

# "#" 안거르고 try-except로 break하는 방법도 있음.

# print(' and '.join([f'{k} {k} glued' for k in glued])) # 오~

import sys

while (1):
    ipt = sys.stdin.readline().rstrip()
    if (ipt == "#"):
        break

    yvy, num, rb = ipt.split()
    former = num[0]
    glued = []
    for i in range(1, 4):
        if ((former == num[i]) and (former not in glued)):
            glued.append(former)
        former = num[i]
    
    if (glued):
        print(f"{glued[0]} {glued[0]} glued", end="")
    if (len(glued) == 2):
        print(f" and {glued[1]} {glued[1]} glued")
    elif (len(glued) == 1):
        print()
