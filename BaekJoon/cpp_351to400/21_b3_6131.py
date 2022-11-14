# 6131

# 소인수분해 해서 약수의 개수가 짝수이면 /2, 홀수이면 1 빼고 /2 하면 된다.

# 다만, 수가 작아서 그냥 for문으로 돌려도 될듯
# range()에 n과 break를 사용하면 for문 횟수를 줄일 수 있다.

import sys

n = int(sys.stdin.readline())

cnt = 0
for B in range(1, 501):
    for A in range(B, 501):
        if (A**2 == B**2 + n):
            cnt += 1

print(cnt)
