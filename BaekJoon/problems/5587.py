# 5587

# geun = [x for x in range(1, 2*n+1) if n not in sang] # 도 가능

import sys

n = int(sys.stdin.readline())
sang = sorted([int(sys.stdin.readline()) for _ in range(n)])

geun = []
for i in range(1, 2*n+1):
    if (i not in sang):
        geun.append(i)

player = [sang, geun]
submit = []
turn = 0
while ((len(player[0]) != 0) and (len(player[1]) != 0)):
    if (len(submit) == 0):
        submit.append(player[turn%2].pop(0))
        turn += 1
    else:
        card_idx = -1
        for each in player[turn%2]:
            if (submit[-1] < each):
                card_idx = player[turn%2].index(each)
                break
        if (card_idx == -1):
            submit = []
        else:
            submit.append(player[turn%2].pop(card_idx))

        turn += 1

print(len(player[1]))
print(len(player[0]))
