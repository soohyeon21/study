# 9865

import sys

n = int(sys.stdin.readline())
for idx in range(1, n+1):
    m = int(sys.stdin.readline())
    card = []
    while (len(card) != m*2):
        ipt = list(map(int, sys.stdin.readline().split()))
        card.extend(ipt)

    score = {'t':0, 'd':0}
    for i in range(m):
        td = sorted([(card[i*2], 't'), (card[i*2+1], 'd')])
        if (td[0][0] == td[1][0]):
            pass
        elif (td[1][0]-1 == td[0][0]):
            if (td[0][0] == 1):
                score[td[0][1]] += 6
            else:
                score[td[0][1]] += td[0][0]+td[1][0]
        else:
            score[td[1][1]] += td[1][0]

    print(f"Game {idx}: Tessa {score['t']} Danny {score['d']}")
