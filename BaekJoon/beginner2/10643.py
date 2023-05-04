# 10643

import sys

pizza = [int(sys.stdin.readline()) for x in range(8)]

total = sum(pizza)
mushroom = []
for i in range(4):
    tmp = sum(pizza[i:i+4])
    mushroom.append(tmp)
    mushroom.append(total - tmp)

print(max(mushroom))
