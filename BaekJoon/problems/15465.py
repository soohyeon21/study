# 15465

import sys

n = int(sys.stdin.readline())

milk = {'B':7, 'E':7, 'M':7}
record = []
for _ in range(n):
    day, name, pm = sys.stdin.readline().split()
    record.append((int(day), name, int(pm)))
record.sort()

change = 0
now_max = 7
now_who = ''
for one in record:
    milk[one[1][0]] += one[2]
    # max값이 변하면 변경o
    ## max값이 변해도, 동일 인물이면 변경x
    ### max값이 변했고, 동일 인물인데, 다른 인물이 또 있으면 변경o
    if ((now_max != max(milk.values())) and ((now_who != one[1][0]) or (now_who == '')) or ((max(milk.values()) == milk[one[1][0]]) and (list(milk.values()).count(milk[one[1][0]]) > 1))):
        now_who = one[1][0]
        change += 1
        now_max = max(milk.values())

print(change)
