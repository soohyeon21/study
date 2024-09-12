# 4678

import sys

def decimal(num):
    deci = 0
    for i in reversed(range(len(num))):
        deci += int(num[i])*(2**(len(num)-i)-1)
    return deci
    

while (1):
    n = sys.stdin.readline().rstrip()
    if (n == "0"):
        break

    deci_num = decimal(n)
    print(deci_num)
