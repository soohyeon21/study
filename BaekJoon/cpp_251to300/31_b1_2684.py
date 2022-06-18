# 2684

# use dictionary

import sys

p = int(sys.stdin.readline())
for _ in range(p):
    coin = sys.stdin.readline().rstrip()
    ttt, tth, tht, thh, htt, hth, hht, hhh = 0, 0, 0, 0, 0, 0, 0, 0
    for i in range(38):
        mer3 = coin[i:i+3]
        if (mer3 == "TTT"):
            ttt += 1
        elif (mer3 == "TTH"):
            tth += 1
        elif (mer3 == "THT"):
            tht += 1
        elif (mer3 == "THH"):
            thh += 1
        elif (mer3 == "HTT"):
            htt += 1
        elif (mer3 == "HTH"):
            hth += 1
        elif (mer3 == "HHT"):
            hht += 1
        elif (mer3 == "HHH"):
            hhh += 1
    print(ttt, tth, tht, thh, htt, hth, hht, hhh)
