# 10610

import sys

n = sorted(list(sys.stdin.readline().rstrip()), reverse=True)

if ('0' not in n):
    print(-1)
elif (sum(map(int, n))%3 == 0):
    print(int(''.join(n)))
else:
    remainder = ['', '', '']
    for rem in range(1, 3):
        for i in range(-1, -n-1, -1):
            if (int(n[i])%3 == rem):
                remainder[rem] = i
                break
            
    if (sum(map(int, n))%3 == 1):
        n.pop(remainder[1])
    elif (sum(map(int, n))%3 == 2):
        n.pop(remainder[2])
        
    print(int(''.join(n)))
