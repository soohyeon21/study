# 1417

# 다솜이와 동일한 수의 최다 득표수를 갖고 있는 후보가 둘 이상이면,
# 그 중에서 한 명의 표만 가져와도 최다 득표로 다솜이가 당선된다.

import sys

n = int(sys.stdin.readline())
cand = [int(sys.stdin.readline()) for x in range(n)]
orin = cand[0]

mxidx = cand.index(max(cand))
while (mxidx != 0):
    cand[0] += 1
    cand[mxidx] -= 1
    mxidx = cand.index(max(cand))

if (cand.count(cand[0]) != 1):
    cand[0] += 1

print(cand[0]-orin)
