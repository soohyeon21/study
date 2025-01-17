# 28323

# '짝-홀-짝-홀-짝-...'인 경우와 '홀-짝-홀-짝-...'인 경우를 찾고, max length 출력

# default 길이를 n으로 놓고, 연속한 수가 똑같이 짝수/홀수일 때마다 -1하는 방법도 있다.

import sys

n = int(sys.stdin.readline())
ai = list(map(int, sys.stdin.readline().split()))

possible = []
for eo in [0, 1]: # 수열의 첫번째가 짝수 or 홀수
    before = eo
    cnt = 0
    for i in range(n):
        if (ai[i]%2 == before):
            cnt += 1
            before = (before+1)%2
    possible.append(cnt)

print(max(possible))
