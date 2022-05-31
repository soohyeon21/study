# 5585

# 문제를 꼼꼼히 읽자. 1000엔에서 물건 값을 뺀 거스름돈에 대한 문제이다.

import sys

money = 1000 - int(sys.stdin.readline())
en = [500, 100, 50, 10, 5, 1]
cnt = 0

for change in en:
    if (money == 0):
        break
    cnt += money//change
    money %= change

print(cnt)
