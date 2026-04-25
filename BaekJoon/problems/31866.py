# 31866

import sys

ipt = tuple(map(int, sys.stdin.readline().split()))

if (ipt in [(5, 0), (2, 5), (0, 2)]):
    print('>')
elif (ipt in [(0, 5), (5, 2), (2, 0)]):
    print('<')
elif (ipt[0] == ipt[1]):
    print('=')
elif ((ipt[0] in [0, 2, 5]) and (ipt[1] not in [0, 2, 5])):
    print('>')
elif ((ipt[0] not in [0, 2, 5]) and (ipt[1] in [0, 2, 5])):
    print('<')
else:
    print('=')
