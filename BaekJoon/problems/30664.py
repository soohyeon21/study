# 30664

import sys

while (1):
    ipt = int(sys.stdin.readline())
    if (ipt == 0):
        break

    if (ipt%42 == 0):
        print("PREMIADO")
    else:
        print("TENTE NOVAMENTE")
