# 10798

import sys

ipt = []
for _ in range(5):
    line = sys.stdin.readline().rstrip()
    line += ' '*(15-len(line))
    ipt.append(line)

result = ""
for i in range(15):
    for j in range(5):
        result += ipt[j][i]

result = result.replace(" ", '')
print(result)
