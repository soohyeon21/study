# 1448

# 뭔가 더 복잡한 구석이 있는 줄 알았는데, 아니었다.

import sys

n = int(sys.stdin.readline())
edge = sorted(list(int(sys.stdin.readline()) for _ in range(n)), reverse=True)

triangle = -1
for i in range(n-2):
    if (edge[i] < edge[i+1]+edge[i+2]):
        triangle = sum(edge[i:i+3])
        break

print(triangle)
