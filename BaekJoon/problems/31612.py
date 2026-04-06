# 31612

import sys

n = int(sys.stdin.readline())
s = sys.stdin.readline().rstrip()

stroke = {'i':2, 'j':2, 'o':1}

cnt = 0
for letter in s:
    cnt += stroke[letter]

print(cnt)
