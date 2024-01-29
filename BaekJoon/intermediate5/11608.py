# 11608

# 간단하게 생각했더니 틀렸다.

import sys

word = sys.stdin.readline().rstrip()
wdict = {}
for letter in word:
    wdict[letter] = wdict.setdefault(letter, 0)
    wdict[letter] += 1

wdict_items = sorted(list(wdict.items()), key=lambda x:x[1])
if (len(wdict_items) <= 2):
    print(0)
else:
    cnt = 0
    while (len(wdict_items) > 2):
        cnt += wdict_items.pop(0)[1]
    print(cnt)
