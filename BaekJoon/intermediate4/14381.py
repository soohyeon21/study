# 14381

# while 대신 for를 쓸 수 있도록 k를 예측할 수 있는 방법이 있을까?

import sys

t = int(sys.stdin.readline())
for i in range(1, t+1):
    n = int(sys.stdin.readline())
    if (n == 0):
        print(f"Case #{i}: INSOMNIA")
        continue

    k = 1
    zero_to_nine = set()
    sleep = 0
    while (1):
        num = str(n*k)
        for each in num:
            zero_to_nine.add(each)
        if (len(zero_to_nine) == 10):
            sleep = num
            break
        k += 1
    print(f"Case #{i}: {sleep}")
