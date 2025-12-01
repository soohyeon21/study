# 11784

import sys

while (1):
    ipt = sys.stdin.readline().rstrip()
    if (ipt == ''):
        break

    rst = ''
    for i in range(len(ipt)//2):
        rst += chr(int(ipt[i*2:i*2+2], 16))

    print(rst)
