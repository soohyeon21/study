# 1251

import sys

word = sys.stdin.readline().rstrip()

newlist = []
for i in range(1, len(word)-1):
    for j in range(i+1, len(word)):
        newlist.append(word[:i][::-1] + word[i:j][::-1] + word[j:][::-1])

newlist.sort()
print(newlist[0])
