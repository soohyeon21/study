# 18409

import sys

n = int(sys.stdin.readline())
word = sys.stdin.readline().rstrip()

cnt = 0
for letter in word:
    if (letter in 'aiueo'):
        cnt += 1

print(cnt)
