# 2386

import sys

while (1):
    inp = sys.stdin.readline().rstrip()
    if (inp == "#"):
        break

    alp = inp[0]
    sen = inp[2:].lower()   

    print(alp, sen.count(alp))
