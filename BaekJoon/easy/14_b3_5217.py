# 5217

import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    pair = ""
    for i in range(1, n//2 + 1):
        if (i != (n-i)):
            if (len(pair) > 2):
                pair += ", "
            pair += str(i) + " " + str(n-i)
    print("Pairs for {}: {}" .format(n, pair))
