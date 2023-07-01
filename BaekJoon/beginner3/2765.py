# 2765

# 소수점 둘째자리까지 꼭 출력하도록 하자.

# 1 mile = 5280 ft
# 1 ft = 12 in

import sys

PI = 3.1415927
cnt = 1
while (1):
    d, c, t = map(float, sys.stdin.readline().split())
    if (c == 0):
        break

    mile = d*PI*c /12/5280
    mph = mile/t*60*60

    print(f"Trip #{cnt}: {round(mile, 2):.2f} {round(mph, 2):.2f}")
    cnt += 1
