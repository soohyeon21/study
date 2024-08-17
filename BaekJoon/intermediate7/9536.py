# 9536

import sys

t = int(sys.stdin.readline())

for _ in range(t):
    total = sys.stdin.readline().split()
    
    while (1):
        ipt = sys.stdin.readline().rstrip()
        if (ipt.split()[0] == "what"):
            print(*total)
            break

        cry = ipt.split()[-1]
        
        tmp = []
        for i in range(len(total)):
            if (total[i] != cry):
                tmp.append(total[i])
        total = tmp
