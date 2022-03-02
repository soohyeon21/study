# 23037

import sys

n = sys.stdin.readline().rstrip()

five = 0
for num in n:
    five += int(num)**5

print(five)
