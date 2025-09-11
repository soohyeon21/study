# 13224

import sys

action = sys.stdin.readline().rstrip()

ball = [1, 0, 0]
for act in action:
    if (act == 'A'):
        ball[0], ball[1] = ball[1], ball[0]
    elif (act == "B"):
        ball[1], ball[2] = ball[2], ball[1]
    elif (act == "C"):
        ball[0], ball[2] = ball[2], ball[0]

print(ball.index(1)+1)
