# 8371

import sys

n = int(sys.stdin.readline())
orig = sys.stdin.readline().rstrip()
pupil = sys.stdin.readline().rstrip()

cnt = 0
for i in range(n):
    if (orig[i] != pupil[i]):
        cnt += 1

print(cnt)
