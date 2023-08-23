# 17273

# 0 or 1만 번갈아 나오게 하려면 1을 더하고 %2하는 방법도 있지만, 1에서 스스로를 빼는 방법도 있다.

import sys

n, m = map(int, sys.stdin.readline().split())
card = []
for _ in range(n):
    f, b = map(int, sys.stdin.readline().split())
    card.append([f, b, 0])
ks = [int(sys.stdin.readline()) for x in range(m)]

for i in range(n):
    for k in ks:
        if (card[i][card[i][2]] <= k):
            card[i][2] = (card[i][2]+1)%2

print(sum(card[j][card[j][2]] for j in range(n)))
