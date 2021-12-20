# 10870

# 흠? def 써서 재귀형식으로 하지 않아도 time over 발생하지 않는가 본데?

import sys

n = int(sys.stdin.readline())

fibo = [0, 1, 1]

for i in range(3, 21):
    if (len(fibo) < n+1):
        fibo.append(fibo[i-1] + fibo[i-2])
    else:
        break
print(fibo[n])
