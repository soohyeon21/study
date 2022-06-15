# 4564

import sys

while (1):
    s = sys.stdin.readline().rstrip()
    if (s == "0"):
        break

    slist = [s]
    while (len(s) != 1):
        val = 1
        for i in range(len(s)):
            val *= int(s[i])
        slist.append(val)
        s = str(val)
    print(*slist)
