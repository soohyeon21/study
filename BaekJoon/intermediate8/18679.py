# 18679

import sys

n = int(sys.stdin.readline())

mdict = {}
for _ in range(n):
    word, minion = sys.stdin.readline().rstrip().split(" = ")
    mdict[word] = minion

t = int(sys.stdin.readline())
for x in range(t):
    k = int(sys.stdin.readline())
    sent = sys.stdin.readline().split()
    for i in range(k):
        print(mdict[sent[i]], end=" ")
    print()
