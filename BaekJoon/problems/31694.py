# 31694

# sort해서 하나씩 비교하다가, 어느 하나가 더 큰 순간이 존재하면 해당인을 우승자로 선정하는 방식도 가능하다.

import sys

def whoWin(score):
    if (ascore[score] > bscore[score]):
        return 'Algosia'
    elif (ascore[score] < bscore[score]):
        return 'Bajtek'
    else:
        return 'remis'


a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))

ascore = {i:a.count(i) for i in reversed(range(11))}
bscore = {j:b.count(j) for j in reversed(range(11))}

win = ""
if (sum(a) > sum(b)):
    win = 'Algosia'
elif (sum(a) < sum(b)):
    win = 'Bajtek'
else:
    for k in reversed(range(11)):
        win = whoWin(k)
        if (win != 'remis'):
            break

print(win)
