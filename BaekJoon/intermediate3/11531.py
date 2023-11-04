# 11531

import sys

penalty = {} # penalty = {prob:[right_wrong, time, try]}

while (1):
    try:
        time, prob, rw = sys.stdin.readline().split()
    except:
        break

    penalty[prob] = penalty.setdefault(prob, [0,0,0])
    if (rw == "right"):
        penalty[prob][0] = 1
        penalty[prob][1] = int(time)
    penalty[prob][2] += 1

plist = list(penalty.items())
total_cnt = 0
total_time = 0
for p in plist:
    if (p[1][0] == 1):
        total_cnt += 1
        total_time += p[1][1] + (p[1][2]-1)*20

print(total_cnt, total_time)
