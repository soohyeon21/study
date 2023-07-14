# 7513

# +=와 for를 같이 쓸 수 있는 방법?

# "Scenario #1:" # ":" 하나도 조심.

import sys

t = int(sys.stdin.readline())
for tnum in range(1, t+1):
    m = int(sys.stdin.readline())
    word = [sys.stdin.readline().rstrip() for x in range(m)]
    n = int(sys.stdin.readline())
    part = [tuple(map(int, sys.stdin.readline().split())) for y in range(n)]

    print(f"Scenario #{tnum}:")
    for person in part:
        pw = ""
        #pw += word[i] for i in person[1:]
        pw2 = "".join(word[i] for i in person[1:]) #
        #plist = list(word[i] for i in person[1:]) #
        #print("".join(plist)) #
        print(pw2)
    print()
