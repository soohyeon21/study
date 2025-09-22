# 15465

# 각 기록마다 display 현황을 조사해서, 직전 display와 비교하는 방법.

import sys

n = int(sys.stdin.readline())

record = []
for _ in range(n):
    order, name, delta = sys.stdin.readline().split()
    record.append((int(order), name, int(delta)))

record.sort()

display_name = ['']
display_score = 7
change = 0
milk = {'Bessie':7, 'Elsie':7, 'Mildred':7}
for cow in record:
    new_name = []
    new_max_score = 0
    milk[cow[1]] += cow[2]

    new_max_score = max(milk.values())
    for one in sorted(milk.items(), reverse=True):
        if (one[1] == new_max_score):
            new_name.append(one[0])

    if (display_name != new_name):
        change += 1
        display_name = new_name
        display_score = new_max_score

print(change)
