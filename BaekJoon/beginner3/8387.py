# 8387

import sys

n = int(sys.stdin.readline())
origin = sys.stdin.readline().rstrip()
pupil = sys.stdin.readline().rstrip()

cnt = 0
for i in range(n):
    if (origin[i] == pupil[i]):
        cnt += 1

print(cnt)
