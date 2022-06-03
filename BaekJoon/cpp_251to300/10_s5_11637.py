# 11637

# ㅋㅋㅋㅋ "="에 조심하자.

import sys

t = int(sys.stdin.readline())
for _ in range(t):
    cand = int(sys.stdin.readline())
    earn = []
    for i in range(cand):
        earn.append(int(sys.stdin.readline()))
    max_earn = max(earn)
    max_person = earn.index(max_earn) + 1
    cowinner = earn.count(max_earn)
    if (cowinner != 1):
        print("no winner")
    elif (max_earn > sum(earn)/2):
        print(f"majority winner {max_person}")
    elif (max_earn <= (sum(earn)/2)):
        print("minority winner %d" %(max_person))
