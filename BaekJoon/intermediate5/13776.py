# 13776

import sys

s = int(sys.stdin.readline())
puzzle = ""
for _ in range(s):
    puzzle += sys.stdin.readline().rstrip()

alpha_order = ""
for letter in puzzle:
    if ((letter not in alpha_order) and (letter != " ")):
        alpha_order += letter

print(alpha_order)
