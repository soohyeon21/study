# 27913

# 매 단계에서 sum하면 25점, 처음에 대문자 개수 구해주고 단계별로 +-1 해주면 100점.
# sum() : O(n)의 시간복잡도.

import sys

n, q = map(int, sys.stdin.readline().split())

rabbit = {}
for i in range(n):
    if (i%10 in [0, 3, 6]):
        rabbit[i] = 1
    else:
        rabbit[i] = 0

up = sum(rabbit.values())
        
for _ in range(q):
    x = int(sys.stdin.readline())
    
    if (rabbit[x-1] == 1):
        rabbit[x-1] = 0
        up -= 1
    elif (rabbit[x-1] == 0):
        rabbit[x-1] = 1
        up += 1

    print(up)
