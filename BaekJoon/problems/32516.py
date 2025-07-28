# 32516

import sys

def cntQuery(t):
    cnt = 0

    # 1. 이미 알려진 문자열에서 팰린드롬이 성립하는지 확인
    for i in range(n):
        if ((t[i] != t[n-1-i]) and ("?" not in [t[i], t[n-1-i]])):
            return cnt

    # 2. 나머지 경우 count
    for i in range(n//2):
        if ((t[i] == "?") or (t[n-1-i] == "?")):
            if ((t[i] == "?") and (t[n-1-i] == "?")):
                cnt += 26
            else:
                cnt += 1

    return cnt


n = int(sys.stdin.readline())
t = sys.stdin.readline().rstrip()

ask = cntQuery(t)
print(ask)
