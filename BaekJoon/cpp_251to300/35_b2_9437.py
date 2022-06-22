# 9437

# 같은 장에 있는 page면 (ex 3, 4) append를 굳이 case를 나누어서 할 필요 없네.

import sys

while (1):
    inp = sys.stdin.readline().rstrip()
    if (inp[0] == "0"):
        break

    page = []
    n, p = map(int, inp.split())
    whole = 1 + n

    if (p % 2 == 0):
        page.append(p-1)
        page.append(whole - p)
        page.append(whole - p + 1)
    elif (p % 2 != 0):
        page.append(p+1)
        page.append(whole - p)
        page.append(whole - p - 1)

    page.sort()
    print(*page)
