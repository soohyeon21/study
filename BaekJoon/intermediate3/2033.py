# 2033

# 문자열 사용 말고 숫자 계산하는 방법도 있다.

import sys

n = int(sys.stdin.readline())
for i in range(1, len(str(n))):
    if (n > 10**i):
        tmp = int(str(n)[:-i])
        if (int(str(n)[-i]) > 4):
            tmp += 1
        n = tmp*10**i
print(n)
