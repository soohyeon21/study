# 6500

# input이 100인 경우, output은 1이어야 함.

import sys

while (1):
    ipt = int(sys.stdin.readline())
    if (ipt == 0):
        break

    num = ipt
    rand = []
    while (num not in rand):
        nnum = int(str(num**2).zfill(8)[2:6])
        if (nnum in rand):
            if (nnum != num):
                rand.append(nnum)
            break
        elif (nnum not in rand):
            rand.append(num)
            num = nnum
            
    print(len(rand))
