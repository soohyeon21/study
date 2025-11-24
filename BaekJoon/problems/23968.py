# 23968

# python3 시간초과, pypy3 정답.

# 슈도 코드 구현 말고 다른 방법으로 푸는 방법?

import sys

def bsort():
    cnt = 0
    state = False
    change = []
    for last in reversed(range(1, n)):
        for i in range(last):
            if (an[i] > an[i+1]):
                cnt += 1
                an[i], an[i+1] = an[i+1], an[i]
                if (cnt == k):
                    state = True
                    change = [an[i], an[i+1]]
                    return change, state
    return change, state


n, k = map(int, sys.stdin.readline().split())
an = list(map(int, sys.stdin.readline().split()))

obj, tf = bsort()

if (tf):
    print(min(obj), max(obj))
else:
    print(-1)
