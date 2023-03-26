# 4388

# a%10의 방법을 써도 되지만, 직전 자리에서 덧셈의 결과로 받아올려지는 수도 잘 확인해야 한다.

import sys

while (1):
    a, b = sys.stdin.readline().split()
    if (a == "0" and b == "0"):
        break

    digita = [0 for x in range(11)]
    digitb = [0 for x in range(11)]
    for ai in range(-1, -len(a)-1, -1):
        digita[ai] = int(a[ai])
    for bi in range(-1, -len(b)-1, -1):
        digitb[bi] = int(b[bi])

    cnt = 0
    for i in range(-1, -11, -1):
        if (digita[i] + digitb[i] >= 10):
            cnt += 1
            digita[i-1] += 1

    print(cnt)
