# 4641

# for문에서 test[:-1]로 범위를 지정해주어도 좋았다.

import sys

while (1):
    test = list(map(int, sys.stdin.readline().split()))
    if (test == [-1]):
        break

    cnt = 0
    for num in test:
        if ((num*2 in test) and (num != 0)):
            cnt += 1

    print(cnt)
