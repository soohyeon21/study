# 11721

import sys

word = sys.stdin.readline().rstrip()
times = len(word)
left = (times // 10 + 1)*10

for i in range(0, left, 10):
    print(word[i:i+10])
