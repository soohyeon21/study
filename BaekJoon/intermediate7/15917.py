# 15917

# 이진수로 바꿔서 첫번째 자리수만 1인지 확인하기

# b를 어떤 수 a의 이진수라고 할 때, (b&(-b) == b)를 만족하면 a는 2의 거듭제곱이라고 한다.

import sys

q = int(sys.stdin.readline())
for _ in range(q):
    a = int(sys.stdin.readline())
    bina = bin(a)
    if (bina.count("1") == 1):
        print(1)
    else:
        print(0)
