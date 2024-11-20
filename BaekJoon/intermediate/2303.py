# 2303

import sys

n = int(sys.stdin.readline())

people = []
for idx in range(1, n+1):
    card = list(map(int, sys.stdin.readline().split()))
    
    mpair = 0
    for i1 in range(5):
        for i2 in range(i1+1, 5):
            for i3 in range(i2+1, 5):
                mpair = max(mpair, (card[i1]+card[i2]+card[i3])%10)

    people.append((idx, mpair))

people.sort(key=lambda x:(-x[1], -x[0]))

print(people[0][0])
