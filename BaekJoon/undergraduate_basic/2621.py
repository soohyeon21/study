# 2621

# 헤헷 결국엔 해결했다~

import sys

color, num = [], []
for _ in range(5):
    col, n = sys.stdin.readline().split()
    color.append(col)
    num.append(int(n))

num.sort()

score = []
# 1
if ((color == [color[0]]*5) and (num == [num[0]+x for x in range(5)])):
    score.append(num[-1] + 900)
# 2
numset = list(set(num))
for i in range(len(numset)):
    if (num.count(numset[i]) == 4):
        score.append(numset[i] + 800)
        break
# 3
if (len(numset) == 2):
    if (num.count(numset[0]) == 3):
        score.append(numset[0]*10 + numset[1] + 700)
    else:
        score.append(numset[1]*10 + numset[0] + 700)
# 4
if (color == [color[0]]*5):
    score.append(num[-1] + 600)
# 5
if (num == [num[0]+x for x in range(5)]):
    score.append(num[-1] + 500)
# 6
for j in range(len(numset)):
    if (num.count(numset[j]) == 3):
        score.append(numset[j] + 400)
        break
# 8
if (len(numset) == 4):
    for v in range(4):
        if (num.count(numset[v]) == 2):
            score.append(numset[v] + 200)
            break
# 7 # 얘가 문제!!
if (len(numset) == 3):
    cnt_numset = sorted([num.count(numset[aa]) for aa in range(3)])
    # len(numset)==3일때만 cnt_numset이 쓸모가 있다. if문 안으로 넣어주니까 ok
    if (cnt_numset == [1, 2, 2]):
        for k in range(3):
            if (num.count(numset[k]) == 1):
                numset.pop(k)
                mmax = max(numset[0], numset[1])
                mmin = min(numset[0], numset[1])
                score.append(mmax*10 + mmin + 300)
                break
# 9
if (score == []):
    score.append(num[-1] + 100)

print(max(score))
