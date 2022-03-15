# 10828

# python은 stack이 없다.

# a = sys.stdin.readline().split()
# 이렇게 하면 a[0], a[1], a[2], ... 이런 식으로 사용하면 된다.

import sys

stk = []
n = int(sys.stdin.readline())
for _ in range(n):
    todo = sys.stdin.readline().rstrip()
    if (todo[:4] == "push"):
        cnt = int(todo[5:])
        todo = todo[:4]
    # 아니면 이런식으로 전개해 나가도 된다.
    #todo = sys.stdin.readline()
    #if (todo[0] == "push"):
    #    stk.append(todo[1])
    

    # push   
    if (todo == "push"):
        stk.append(cnt)
    # pop
    elif (todo == "pop"):
        if (stk == []):
            print(-1)
        else:
            print(stk.pop())
    # size
    elif (todo == "size"):
        print(len(stk))
    # empty
    elif (todo == "empty"):
        if (len(stk) == 0):
            print(1)
        else:
            print(0)
    # top
    elif (todo == "top"):
        if (len(stk) == 0):
            print(-1)
        else:
            print(stk[-1])
