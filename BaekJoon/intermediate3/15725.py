# 15725

# 계수가 음수인 경우 주의

import sys

def checkPoly(plist):
    for p in plist:
        if ("x" in p):
            if (p == "x"):
                print(1)
            elif (p == "-x"):
                print(-1)
            else:
                print(p[:-1])
            return
    print(0)
    return

poly = sys.stdin.readline().rstrip().replace("-", " -").replace("+", " ").split()

checkPoly(poly)
