# 2476

# 같은 것 3개/같은 것 2개 case x2/셋 다 다름

n = int(input())

prize = []

for _ in range(n):
    dice = list(map(int, input().split()))
    if (dice.count(dice[0]) == 3):
        prize.append(10000 + dice[0] * 1000)
    elif (dice.count(dice[0]) == 2):
        prize.append(1000 + dice[0] * 100)
    elif (dice.count(dice[1]) == 2):
        prize.append(1000 + dice[1] * 100)
    elif ((dice.count(dice[0]) == 1) and (dice.count(dice[1]) == 1)):
        prize.append(max(dice) * 100)
print(max(prize))
