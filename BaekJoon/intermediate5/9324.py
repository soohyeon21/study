# 9324

import sys

t = int(sys.stdin.readline())

for _ in range(t):
    m = sys.stdin.readline().rstrip()

    check = {}
    now = ""
    state = True
    for letter in m:
        check[letter] = check.setdefault(letter, 0)
        check[letter] += 1
        if (check[letter] == 3):
            now = letter
        if (check[letter] == 4):
            if (now != letter):
                state = False
                break
            else:
                check[letter] = 0
    if (3 in check.values()):
        state = False

    if (state):
        print("OK")
    else:
        print("FAKE")
