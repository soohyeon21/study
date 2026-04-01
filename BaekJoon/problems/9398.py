# 9398

import sys

n = int(sys.stdin.readline())

for _ in range(n):
    given = sys.stdin.readline().rstrip()

    state = False
    shrt = 0
    for slen in range(6, len(given)+1):
        for start in range(len(given)-slen+1):
            up, low, dig = False, False, False
            for letter in given[start:start+slen]:
                if (letter.isupper()):
                    up = True
                if (letter.islower()):
                    low = True
                if (letter.isnumeric()):
                    dig = True
            state = up and low and dig
            if (state):
                shrt = slen
                break
        if (state):
            break

    print(shrt)
