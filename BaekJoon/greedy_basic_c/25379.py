# 25379

# list.count() # O(n)

# oddeven == 0 # 홀-짝 case
# oddeven == 1 # 짝-홀 case

# 홀/짝 개수 세서 더하는 방식

import sys

n = int(sys.stdin.readline())
an = list(map(int, sys.stdin.readline().split()))
oz = [0 if an[x]%2==0 else 1 for x in range(n)]

moves = []
for oddeven in [0, 1]:
    move = 0
    oe_cnt = 0
    for i in range(n):
        if (oz[i] == (1-oddeven)):
            move += oe_cnt
        elif (oz[i] == oddeven):
            oe_cnt += 1
    moves.append(move)
    
print(min(moves))
