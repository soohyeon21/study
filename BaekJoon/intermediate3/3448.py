# 3448

# range(n) 조심

# round(num, 어디서) # 음수는 정수부분 반올림, 양수는 소수부분 반올림

import sys

n = int(sys.stdin.readline())
for _ in range(n):
    ch = ""
    while (1):
        tmp = sys.stdin.readline().replace("\n", "")
        if (tmp == ""):
            break

        ch += tmp

    a = len(ch)
    r = a - ch.count("#")
    ra = round(r/a*100, 1)
    if (ra == int(ra)):
        ra = int(ra)

    print(f"Efficiency ratio is {ra}%.")
