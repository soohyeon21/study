# 20362

import sys

n, s = sys.stdin.readline().split()

log = []
answer = ""
for _ in range(int(n)):
    name, response = sys.stdin.readline().split()
    if (name == s):
        answer = response
    log.append((name, response))

cnt = 0
for i in range(int(n)):
    if (log[i][0] == s):
        break
    if (log[i][1] == answer):
        cnt += 1

print(cnt)
