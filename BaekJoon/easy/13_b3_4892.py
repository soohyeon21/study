# 4892

import sys

cnt = 1
chk = ""
while (True):
    n0 = int(sys.stdin.readline())
    if (n0 == 0):
        break
    n1 = 3 * n0

    if (n1 % 2 == 0):
        chk = "even"
        n2 = n1 // 2
    else:
        chk = "odd"
        n2 = (n1+1) // 2
    n3 = 3 * n2
    n4 = n3 // 9
    #rst = 2*n4 if (n1 % 2 == 0) else (2*n4 +1)
    print("{}. {} {}" .format(cnt, chk, n4))
    cnt += 1
