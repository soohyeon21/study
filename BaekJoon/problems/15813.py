# 15813

import sys

length = int(sys.stdin.readline())
name = sys.stdin.readline().rstrip()

score = 0
for letter in name:
    score += ord(letter)-64

print(score)
