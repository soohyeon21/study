# 17838

# def 3에서 낱개의 문자가 1개만 사용된 경우도 있을 수 있으므로 ab[1]대신 ab[-1]
# 014, 2356번째가 같은지 확인하는 방법도 가능
# 0, 2번째를 각각 특정 문자로 replace해서 지정된 특정문자 조합과 일치하는지 확인 ex)@@!!@!!

# 그냥 if-elif-else문으로 중간에 조건이 맞지 않을때마다 0 출력하는 방법도 있다.

# int(True) # 1
# int(False) # 0

import sys

t = int(sys.stdin.readline())
for _ in range(t):
    cmd = sys.stdin.readline().rstrip()
    state = True

    # def 1
    if (len(cmd) != 7):
        state = False

    # def 2
    if (len(set(cmd)) != 2):
        state = False

    # def 3
    ab = list(set(cmd))
    a = ab[0]
    b = ab[-1]
    if ((cmd != a+a+b+b+a+b+b) and (cmd != b+b+a+a+b+a+a)):
        state = False

    print(int(state))
