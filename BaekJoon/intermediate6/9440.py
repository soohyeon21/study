# 9440

import sys

while (1):
    ipt = sys.stdin.readline().rstrip()
    if (ipt == "0"):
        break
    
    zeros = ipt.count("0")
    half_z = zeros//2
    
    ipt = ipt.replace("0", "").split()
    n = int(ipt[0])
    ipt = ipt[1:]
    
    num1 = ipt[0] + "0"*(zeros-half_z)
    num2 = ipt[1] + "0"*half_z
    for i in range(len(ipt)-zeros-3):
        if (i%2 == 0):
            num1 += ipt[i]
        elif (i%2 != 0):
            num2 += ipt[i]
    
