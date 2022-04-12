# 2484

# sort를 사용할 수 있다.

# len(sdice) == 2일 때, list[0]과 list[1]의 값을 비교해서 전개하여도 된다.
# len(sdice) == 3일 때, 마찬가지로 list의 값 비교로 전개 가능하다.

import sys

n = int(sys.stdin.readline())
price = []
for _ in range(n):
    dice = list(map(int, sys.stdin.readline().split()))
    sdice = set(dice)
    ldice = list(sdice)
    if (len(sdice) == 1): # 동전 모두 같을 때
        price.append(50000 + ldice[0]*5000)
    elif (len(sdice) == 2):
        if (dice.count(ldice[0]) == 1): # 동전 3개 같을 때1
            price.append(10000 + ldice[1]*1000)
        elif (dice.count(ldice[0]) == 3): # 동전 3개 같을 때2
            price.append(10000 + ldice[0]*1000)
        elif (dice.count(ldice[0]) == 2): # 동전 2쌍 서로 같을 때
            price.append(2000 + 500*(ldice[0] + ldice[1]))
    elif (len(sdice) == 3): # 동전 2개 같을 때
        target = 0
        for i in range(3):
            if (dice.count(ldice[i]) == 2):
                target = ldice[i]
        price.append(1000 + target*100)
    else: # 모든 동전이 다 다를 때
        price.append(max(dice)*100)

print(max(price))
##print(price)
