# 3474

# 오른쪽 끝의 연속된 0의 개수는 10의 제곱의 수만큼.
# 그런데 10은 2와 5의 곱으로 이루어지는데, 5의 개수가 2의 개수보다 훨씬 적기 때문에
# 5가 총 몇 번 곱해지는 것인지를 찾으면 되는 문제.

import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    cnt = 0
    five = 1
    while (5**five <= n):
        cnt += n//(5**five)
        five += 1
    print(cnt)
