# 4158

# "입력은 여러 개의 테스트 케이스로 이루어져 있다."

# 이분 탐색으로 풀 수도 있다고 한다.

import sys

while (1):
    n, m = map(int, sys.stdin.readline().split())
    if ((n == 0) and (m == 0)):
        break

    cd = {}
    for i in range(n+m):
        cd_num = int(sys.stdin.readline())
        cd[cd_num] = cd.setdefault(cd_num, 0)
        cd[cd_num] += 1

    both = list(cd.values()).count(2)
    print(both)
