# 10845

import sys

n = int(sys.stdin.readline())

que = []
for _ in range(n):
    ipt = sys.stdin.readline().split()
    word = ipt[0]

    if (word == "push"):
        que.append(ipt[1])

    elif (word == "pop"):
        if (len(que) == 0):
            print(-1)
        else:
            print(que.pop(0))

    elif (word == "size"):
        print(len(que))

    elif (word == "empty"):
        if (len(que) == 0):
            print(1)
        else:
            print(0)

    elif (word == "front"):
        if (len(que) == 0):
            print(-1)
        else:
            print(que[0])

    elif (word == "back"):
        if (len(que) == 0):
            print(-1)
        else:
            print(que[-1])
