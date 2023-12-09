# 4383

import sys

while (1):
    ipt = sys.stdin.readline().rstrip()
    if (ipt == ""):
        break

    ipt = list(map(int, ipt.split()))
    n = ipt[0]
    nlist = ipt[1:]

    isJolly = set(abs(nlist[i]-nlist[i+1]) for i in range(n-1))
    if (n == 1):
        print("Jolly")
    elif (sorted(list(isJolly)) == [x for x in range(1, n)]):
        print("Jolly")
    else:
        print("Not jolly")
