# 10179

# "나누어떨어지지 않을 때는 소수점 셋째 자리에서 반올림해서 둘째 자리까지 출력"
# 따라서 round() 쓰지 않고 그냥 %.2f 해도 되는 일이었음.

# round()는 python의 내장 함수.

import sys

t = int(sys.stdin.readline())
for _ in range(t):
    cost = float(sys.stdin.readline())
    disc = round(cost*0.8, 2)
    print("$%.2f" %(disc))
