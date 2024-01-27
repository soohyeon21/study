# 9313

# "문자열".zfill(자릿수)
# zfill로 채워진 0은 문자열의 앞에 붙음.

import sys

while (1):
    num = int(sys.stdin.readline())
    if (num == -1):
        break

    binum = bin(num)
    zeros = "0"*(34-len(binum)) if (len(binum)<34) else ""
    renum = int((zeros+binum[2:])[::-1], 2)
    print(renum)
