# 11117

import sys

t = int(sys.stdin.readline())
for _ in range(t):
    ipt = sys.stdin.readline().rstrip()
    box = {chr(num):0 for num in range(65, 91)}
    for letter in ipt:
        box[letter] += 1

    n = int(sys.stdin.readline())
    for __ in range(n):
        cookie = sys.stdin.readline().rstrip()
        cookie_set = list(set(cookie))
        state = True
        for c in cookie_set:
            if (cookie.count(c) > box[c]):
                state = False
                break

        if (state):
            print("YES")
        else:
            print("NO")
