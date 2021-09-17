# 2480

# cnt == 2일때, 그냥 sort해서 1번째 element 가져다 써도 되겠다.

dice = list(map(int, input().split()))

dic = set(dice)
cnt = len(dic)
if (cnt == 3): # 다 다름
    prize = max(dice) * 100
elif (cnt == 2): # 2개 같음
    cnt1 = dice.count(dice[0])
    if (cnt1 == 2):
        prize = 1000 + dice[0] * 100
    else:
        prize = 1000 + dice[1] * 100
else: # 3개 다 같음
    prize = 10000 + dice[0] * 1000
print(prize)
