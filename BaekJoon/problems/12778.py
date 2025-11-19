# 12778

import sys

t = int(sys.stdin.readline())
for _ in range(t):
    m, s = sys.stdin.readline().split()
    ipt = sys.stdin.readline().split()

    result = []
    if (s == "C"):
        for i in range(int(m)):
            result.append(ord(ipt[i])-64)
    elif (s == "N"):
        for j in range(int(m)):
            result.append(chr(int(ipt[j])+64))

    print(*result)
