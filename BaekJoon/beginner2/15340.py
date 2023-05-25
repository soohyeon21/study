# 15340

import sys

while (1):
    call, data = map(int, sys.stdin.readline().split())
    if ((call == 0) and (data == 0)):
        break
    
    print(min(30*call+40*data, 35*call+30*data, 40*call+20*data))
