# 24416

# 직접 recursive fibo를 구현하면 시간 초과.

# 코드1은 결국 n번째 피보나치 수를 의미한다.

# UnboundLocalError: cannot access local variable 'fibcnt' where it is not associated with a value

import sys

def dp(n):
    f = [0, 1, 1]
    for i in range(3, n+1):
        f.append(f[i-1] + f[i-2])
    return f[n]

n = int(sys.stdin.readline())
cnt1 = dp(n)
cnt2 = n-2
print(cnt1, cnt2)
