# 2160

# i와 j의 range를 다르게 설정하면 계산 횟수를 줄일 수 있다.

# min((3, 44, 55), (1, 100, 10000)) # (1, 100, 10000)
# sort 말고 min 써도 된다.

import sys

n = int(sys.stdin.readline())
painting = [[sys.stdin.readline().rstrip() for x in range(5)] for xx in range(n)]
sim = []

for i in range(n):
    for j in range(n):
        if (i==j):
            continue
        diff = 0
        for line in range(5):
            for single in range(7):
                if (painting[i][line][single] != painting[j][line][single]):
                    diff += 1
        sim.append((min(i+1, j+1), max(i+1, j+1), diff))

sim.sort(key=lambda x:x[2])
print(sim[0][0], sim[0][1])
