# 16769

import sys

def pour():
    for i in range(1, 101):
        tmp = min(buck[i%3][0], buck[i%3][1]+buck[(i-1)%3][1])
        buck[(i-1)%3][1] -= tmp - buck[i%3][1]
        buck[i%3][1] = tmp
                
        pair = tuple(buck[x][1] for x in range(3))
        states.append(pair)

buck = [list(map(int, sys.stdin.readline().split())) for _ in range(3)]

states = []
pour()

print(*states[-1], sep="\n")
