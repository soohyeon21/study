# 14405

import sys

s = sys.stdin.readline().rstrip().replace('pi', ' ').replace('ka', ' ').replace('chu', ' ').replace(' ', '')

if (len(s) > 0):
    print('NO')
else:
    print("YES")
