# 17011

import sys

n = int(sys.stdin.readline())
for _ in range(n):
    line = sys.stdin.readline().rstrip()
    c = line[0]
    cnt = 1
    encode = []
    for i in range(1, len(line)):
        if (c == line[i]):
            cnt += 1
        else:
            encode.extend([cnt, c])
            c = line[i]
            cnt = 1
    encode.extend([cnt, c])
    print(*encode)
