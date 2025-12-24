# 11478

import sys

s = sys.stdin.readline().rstrip()

sets = set()
for i in range(len(s)):
    for j in range(i+1, len(s)+1):
        sets.add(s[i:j])

print(len(sets))
