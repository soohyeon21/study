# 4072

import sys

while (1):
    ipt = sys.stdin.readline().rstrip()
    if (ipt == "#"):
        break

    for word in ipt.split():
        print(word[::-1], end=' ')
    print()
