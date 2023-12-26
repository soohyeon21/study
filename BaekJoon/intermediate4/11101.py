# 11101

# "이때 꿍은 각 조건들을 병렬적으로 만족시킬 수 있다고 생각한다."

import sys

t = int(sys.stdin.readline())
for _ in range(t):
    vari = sys.stdin.readline().split(",")
    need = {}
    for elem in vari:
        subj, num = elem.split(":")
        need[subj] = int(num)
        
    and_or = sys.stdin.readline().rstrip().split("|")
    or_cnt = []
    for one in and_or:
        and_con = one.split("&")
        sub_total = 0
        for con in and_con:
            sub_total = max(sub_total, need[con])
        or_cnt.append(sub_total)

    print(min(or_cnt))
