# 2816

# 4개 버튼을 반드시 모두 사용하거나, 가장 적게 사용해야 하는 문제는 아니다.
# 따라서, 풀이는 정말정말 다양하다.

import sys

def move(chan, rank):
    global now
    global order
    
    kbs = tv.index(chan)
    if (now < kbs):
        now += kbs
        order.append("1"*kbs)
    order.append("4"*(now-rank+1))
    now = rank-1
    tv.insert(rank, tv.pop(kbs))

n = int(sys.stdin.readline())
tv = []
for _ in range(n):
    tv.append(sys.stdin.readline().rstrip())

now = 0
order = []
move("KBS1", 1)
move("KBS2", 2)

print(*order, sep="")
