# 9711

# append 하지 말고 0으로 fibo 10001개 채워놓은 다음에 해당 index의 값 변경하는 방법도 있다.

import sys

t = int(sys.stdin.readline())

fibo = [1, 1, 2, 3, 5]

for idx in range(1, t+1):
    p, q = map(int, sys.stdin.readline().split())

    value = 0
    if (len(fibo) < p):
        for i in range(len(fibo), p+1):
            fibo.append(fibo[i-1] + fibo[i-2])

    value = fibo[p-1]

    print(f"Case #{idx}: {value % q}")
