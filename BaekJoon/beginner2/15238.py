# 15238

# dictionary도 있었으나, value로 key 찾기ㅎ
# sort, key, lambda 오랜만인데 잘 썼다!

import sys

n = int(sys.stdin.readline())
word = sys.stdin.readline().rstrip()
wset = set(word)
cand = []

for comp in wset:
    cand.append((comp, word.count(comp)))
cand.sort(key = lambda x: x[1])
print(cand[-1][0], cand[-1][1])
