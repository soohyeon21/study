# 27962

# 뒤집지 않은 두 부분 문자열 이어야 한다.

import sys

n = int(sys.stdin.readline())
sent = sys.stdin.readline().rstrip()

state = False
for wlen in range(1, n+1):
    left = sent[:wlen]
    right = sent[-wlen:]

    diff = 0
    for i in range(wlen):
        if (left[i] != right[i]):
            diff += 1

    if (diff == 1):
        state = True
        break

if (state):
    print('YES')
else:
    print('NO')
