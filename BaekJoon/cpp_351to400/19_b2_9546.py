# 9546

# 첫 탑승 인원은 홀수명일 수 밖에 없음.

# 1 <= k <= 30이니까 O() 신경 안쓰고 했다.

import sys

def station(num):
    if (num == 1):
        return 1
    else:
        before = station(num-1)
        now = 2*before + 1
        return now

n = int(sys.stdin.readline())
for _ in range(n):
    k = int(sys.stdin.readline())
    print(station(k))
