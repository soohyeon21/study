# 20920

# sorted() 할 때 굳이 list()를 사용하지 않아도 괜찮다.

# "PyPy3는 Python3와 같은 문법을 가지면서 일반적으로 더 빠르게 동작한다.
# 연산량이 많은 문제에서 Python을 사용하고자 한다면 PyPy로 제출하는 것을 권장한다."

import sys

n, m = map(int, sys.stdin.readline().split())

wdict = {}
for _ in range(n):
    word = sys.stdin.readline().rstrip()
    if (len(word) < m):
        continue

    wdict[word] = wdict.setdefault(word, 0)
    wdict[word] += 1

note = sorted(list(wdict.items()), key=lambda x:(-x[1], -len(x[0]), x))

for one in note:
    print(one[0])
