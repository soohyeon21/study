# 8892

import sys

def findPal(word):
    for i in range(len(word)-1):
        for j in range(i+1, len(word)):
            cand = possPW(word[i], word[j])
            for one in cand:
                if (one == one[::-1]):
                    return one
    return 0

def possPW(w1, w2):
    return [w1+w2, w2+w1]


t = int(sys.stdin.readline())
for _ in range(t):
    k = int(sys.stdin.readline())
    word = [sys.stdin.readline().rstrip() for x in range(k)]

    result = findPal(word)
    print(result)
