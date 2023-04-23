# 9517

# totalt에서 time을 빼주면서 음수가 되는지 확인하는 방법도 있다.

import sys

k = int(sys.stdin.readline())
n = int(sys.stdin.readline())

totalt = 3*60 + 30
spendt = 0
who = k-1

for _ in range(n):
    time, ans = sys.stdin.readline().split()
    time = int(time)
    spendt += time

    if (spendt >= totalt):
        print(who+1)
        break

    if (ans == "T"):
        who = (who+1)%8
