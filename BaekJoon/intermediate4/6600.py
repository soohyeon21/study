# 6600

# 웬만하면 except EOFError보다는 그냥 except가 나은듯.

# try-except 처리는 while문 안에서 입력에 해당하는 부분에 대해서만 적용시키자.

import sys
import math

while (1):
    try:
        x1, y1, x2, y2, x3, y3 = map(float, sys.stdin.readline().split())
    except: # except EOFError로 하면 '런타임 에러(ValueError)' 발생
        break

    # 외심(a, b)
    # b
    b = ((x2**2-x1**2+y2**2-y1**2)*(2*x3-2*x2) - (x3**2-x2**2+y3**2-y2**2)*(2*x2-2*x1))\
    / ((2*y2-2*y3)*(2*x2-2*x1) - (2*y1-2*y2)*(2*x3-2*x2)) # ZeroDivisionError 발생 불가
    #a
    try:
        a = ((2*y2-2*y3)*b + (x3**2-x2**2+y3**2-y2**2)) / (2*x3-2*x2)
    except ZeroDivisionError: # x1, x2, x3가 모두 같을 수는 없기 때문
        a = ((2*y1-2*y2)*b + (x2**2-x1**2+y2**2-y1**2)) / (2*x2-2*x1)
    r = math.sqrt((x1-a)**2+(y1-b)**2)
    periphery = 2*math.pi*r

    #print(f"{periphery:.2f}")
    print(round(periphery, 2))
