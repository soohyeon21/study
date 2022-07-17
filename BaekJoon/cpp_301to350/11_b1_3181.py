# 3181

# in+continue 말고 not in을 써도 됐다.

import sys

nouse = ['i', 'pa', 'te', 'ni', 'niti', 'a', 'ali', 'nego', 'no', 'ili']

ipt = sys.stdin.readline().split()

short = ""
for i in range(len(ipt)):
    if ((i == 0) and (ipt[0] in nouse)):
        short += ipt[0][0]
    if (ipt[i] in nouse):
        continue
    short += ipt[i][0]

short = short.upper()
print(short)
