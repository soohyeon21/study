# 17388

# min(s, k, h)의 return 값은 s/k/h 이다.
# 부등식으로 if 조건 처리하는 경우도 있다.

import sys

par = list(map(int, sys.stdin.readline().split()))
if (sum(par) < 100):
    chk = par.index(min(par))
    if (chk == 0):
        print("Soongsil")
    elif (chk == 1):
        print("Korea")
    else:
        print("Hanyang")
else:
    print("OK")
