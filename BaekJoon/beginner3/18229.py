# 18229

# def, return을 쓰면 break 2번 사용 않고 곧장 끝낼 수 있다.

import sys

n, m, k = map(int, sys.stdin.readline().split())
hand = [list(map(int, sys.stdin.readline().split())) for x in range(n)]
person = [0 for y in range(n)]
who, th = -1, -1
state = True

for i in range(m):
    for j in range(n):
        person[j] += hand[j][i]
        if (person[j] >= k):
            who = j+1
            th = i+1
            state = False
            break
    if (state == False):
        break

print(who, th)
