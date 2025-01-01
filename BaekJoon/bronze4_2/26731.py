# 26731

import sys

alpha = sys.stdin.readline().rstrip()

within = []
for letter in alpha:
    within.append(ord(letter))

for num in range(65, 91):
    if (num not in within):
        print(chr(num))
        break
