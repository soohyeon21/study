# 16466

# 첫 티켓팅에서 팔린 티켓들이 모두 연속의 번호인 경우도 있을 수 있다.

# (num == ticket1[i])일때 t+=1하고, else이면 break하고 print(num)하는 방법도 있다.

import sys

def findTicket(ticket1):
    num = 1
    for i in range(n):
        if (num < ticket1[i]):
            print(num)
            return
        else:
            num += 1
    print(num)
    return

n = int(sys.stdin.readline())
tlist = sorted(list(map(int, sys.stdin.readline().split())))
findTicket(tlist)
