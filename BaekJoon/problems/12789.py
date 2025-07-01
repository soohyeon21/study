# 12789

# 간단하게 생각하자.

import sys

def snack():
    aside = []
    now = 1

    for i in range(n):
        if (num[i] == now):
            now += 1
        elif (num[i] != now):
            aside.append(num[i])

        while (aside):
            if (aside[-1] == now):
                aside.pop()
                now += 1
            elif (aside[-1] != now):
                break

    if (aside):
        return "Sad"
    else:
        return "Nice"
        

n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))

state = snack()
print(state)
