# 14535

# malpha는 밖으로 빼도 될듯.

import sys

num = 1
while (1):
    n = int(sys.stdin.readline())
    if (n == 0):
        break

    month = {mon:0 for mon in range(1, 13)}
    malpha = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    for _ in range(n):
        dd, mm, year = map(int, sys.stdin.readline().split())
        month[mm] += 1

    print(f"Case #{num}:")
    for i in range(12):
        print(f"{malpha[i]}:{'*'*month[i+1]}")
    
    num += 1
