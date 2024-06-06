# 9612

# lambda x:(x[1], x[0]) 순서로 sort하고 마지막 element를 선택하는 방법도 있다.

import sys

n = int(sys.stdin.readline())

wdict = {}
for _ in range(n):
    word = sys.stdin.readline().rstrip()
    wdict[word] = wdict.setdefault(word, 0)
    wdict[word] += 1

lexico = sorted(list(wdict.items()), key=lambda x:(-x[1], x[0]))

most = []
for one in lexico:
    if (one[1] == lexico[0][1]):
        most.append(one)
    else:
        break
print(most[-1][0], most[-1][1])
