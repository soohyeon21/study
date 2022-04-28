# 1076

# resist 값 3개를 각각 variable에 담았으면 조금 더 빨리 돌아갈 수 있으려나.

import sys

color = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']

resist = []
for _ in range(3):
    resist.append(sys.stdin.readline().rstrip())

value = int(str(color.index(resist[0])) + str(color.index(resist[1])))
mul = value * (10**color.index(resist[2]))
print(mul)
