# 14468

# 동일 이름 사이에 다른 이름이 짝 없이 끼어있으면 만난다.

import sys

cows = sys.stdin.readline().rstrip()

##for i in range(65, 91):
##    cows = cows.replace(str(chr(i))*2, '')

coord = {}
alpha = {}
for k in range(len(cows)):
    coord[k] = cows[k]
    alpha[cows[k]] = alpha.setdefault(cows[k], [])
    alpha[cows[k]].append(k)

pair = []
for p in range(len(cows)):
    st, ed = alpha[cows[p]]
    for check in range(st+1, ed):
        if (((st<alpha[coord[check]][0]<ed) and not(st<alpha[coord[check]][1]<ed)) or (not(st<alpha[coord[check]][0]<ed) and (st<alpha[coord[check]][1]<ed))):
            if ((cows[p]+coord[check] not in pair) and (coord[check]+cows[p] not in pair)):
                pair.append(cows[p]+coord[check])

print(len(pair))
