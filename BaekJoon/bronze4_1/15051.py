# 15051

# 3개 경우 밖에 없으므로 일일이 계산해서 min값을 구해줘도 된다.

import sys

ai = list(int(sys.stdin.readline()) for _ in range(3))

tconsum = []
for i in range(3):
    total = 0
    for exp in range(3):
        if (i != exp):
            total += ai[exp] * 2**abs(i-exp)
    tconsum.append(total)

print(min(tconsum))
