# 11047

# continue 부분은 넣어주면 시간 4ms 단축 가능. 있어도 없어도 no matter
# 으잉 근데 break 위치 k%=wallet[i] 밑으로 바꿔주면 다시 68ms가 되어버린다...

# list에 음수 index로 접근시, for문 range에서 끝부분은 포함되지 않는다는 것 주의

# 입력 예시가 10개일 뿐, 항상 10개가 아니다. 꼼꼼히 확인할 것.

import sys

n, k = map(int, sys.stdin.readline().split())

wallet = []
for _ in range(n):
    coin = int(sys.stdin.readline())
    if (coin > k):
        break
    wallet.append(coin)

cnt = 0
for i in range(-1, -1*len(wallet) - 1, -1):
    if (k == 0):
        break
##    if (wallet[i] > k):
##        continue
    cnt += k // wallet[i]
    k %= wallet[i]
##    print(k, cnt)
print(cnt)
