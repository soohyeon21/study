# 2993

import sys

word = sys.stdin.readline().rstrip()

wdict = []
for i in range(len(word)-2):
    for j in range(i+1, len(word)-1):\
        wdict.append(word[:i+1][::-1]+word[i+1:j+1][::-1]+word[j+1:][::-1])
wdict.sort()

print(wdict[0])
