# 27522

# score=[10, 8, 6, 5, 4, 3, 2, 1]로 해서 for문으로 처리할 수도 있다.
# append는 one argument에 대해서만 처리 가능.
# sort key에 lambda 사용시 순서 괄호로 묶어주기.

import sys

record = []
for i in range(8):
    t, team = sys.stdin.readline().split()
    record.append(t.split(":")+[team])
record.sort(key=lambda x:(x[0], x[1], x[2]))

score = 6
for j in range(2, 8):
    record[j].append(score)
    score -= 1
record[0].append(10)
record[1].append(8)

blue = 0
red = 0
for k in range(8):
    if (record[k][3] == "B"):
        blue += record[k][-1]
    elif (record[k][3] == "R"):
        red += record[k][-1]
first = record[0][3]

win = ""
if (blue == red):
    win = "Red" if (first == "R") else "Blue"
elif (blue > red):
    win = "Blue"
elif (blue < red):
    win = "Red"

print(win)
