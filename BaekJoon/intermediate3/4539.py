# 4539

# #2033이랑 같은 문제인듯.
# 이번에는 숫자 계산으로 풀어봤다.

# list로 각 자릿수를 분리하여 푸는 방법 # 자릿수가 10이 넘어도 된다. 어차피 list로 분리되어 있으니까!

import sys

n = int(sys.stdin.readline())
for _ in range(n):
    x = int(sys.stdin.readline())
    times = 10
    while (x > times):
        if (x%times//(times*0.1) > 4): # or if (x%times >= times/2):
            x = (x//times + 1)*times
        else:
            x = x//times * times
        times *= 10
    print(x)
