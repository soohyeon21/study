# 10866

import sys

n = int(sys.stdin.readline())

deq = []
for _ in range(n):
    inp = sys.stdin.readline().split()
    word = inp[0]

    if (word == "push_front"):
        deq.insert(0, inp[1])

    elif (word == "push_back"):
        deq.append(inp[1])

    elif (word == "pop_front"):
        if (len(deq) == 0):
            print(-1)
        else:
            print(deq.pop(0))

    elif (word == "pop_back"):
        if (len(deq) == 0):
            print(-1)
        else:
            print(deq.pop())

    elif (word == "size"):
        print(len(deq))

    elif (word == "empty"):
        if (len(deq) == 0):
            print(1)
        else:
            print(0)

    elif (word == "front"):
        if (len(deq) == 0):
            print(-1)
        else:
            print(deq[0])

    elif (word == "back"):
        if (len(deq) == 0):
            print(-1)
        else:
            print(deq[-1])
