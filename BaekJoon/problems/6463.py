# 6463

import sys

sys.set_int_max_str_digits(10**6)

fact = [1]+[0 for _ in range(10000)]
for i in range(1, 10001):
    fact[i] = fact[i-1]*i

while (1):
    n = sys.stdin.readline().rstrip()
    if (n == ''):
        break

    n = int(n)
    last = str(int(str(fact[n])[::-1]))[0]
    print(f"{n:5d} -> {last}")
