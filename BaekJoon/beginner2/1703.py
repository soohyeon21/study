# 1703

# asterisk + variable

import sys

while (1):
    case = list(map(int, sys.stdin.readline().split()))
    if (case == [0]):
        break

    branch = 1
    for i in range(1, 2*case[0]+1, 2):
        branch *= case[i]
        branch -= case[i+1]

    print(branch)
