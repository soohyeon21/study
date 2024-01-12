# 24417

# fibonacci1()은 메모리 초과

# fibonacci()도 PyPy3로 해야 정답, Python3는 시간 초과
# 그나마도 def 안에서 % 연산해야 정답.

import sys

def fibonacci1(n):
    f = [0, 1, 1] + [0 for _ in range(2*10**8)]
    for i in range(3, n+1):
        f[i] = f[i-1] + f[i-2]
    return f[n]

def fibonacci(n):
    a, b = 1, 1
    for i in range(3, n+1):
        b, a = (a+b)%1000000007, b
    return b

n = int(sys.stdin.readline())
cnt1 = n-2
cnt2 = fibonacci(n)
print(cnt2, cnt1)
