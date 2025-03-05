# 11313

import sys

n = int(sys.stdin.readline())
participant = []
for _ in range(n):
    first, last = sys.stdin.readline().split()
    participant.append((first, last))
participant.sort(key=lambda x:(x[1], x[0]))

findName = {}
for i in range(n):
    findName[i] = participant[i]
findNum = {}
for j in range(n):
    findNum[participant[j]] = j

q = int(sys.stdin.readline())
for _ in range(q):
    first, last = sys.stdin.readline().split()
    foundNum = findNum[(first, last)]
    for k in range(3):
        quot = foundNum//3
        rem = foundNum%3
        othersNum = quot*3 + k
        if (othersNum != foundNum):
            print(*findName[othersNum], sep=' ')
