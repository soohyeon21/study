# 5543

burger = []
beverage = []

for _ in range(3):
    burger.append(int(input()))

for i in range(2):
    beverage.append(int(input()))

price = min(burger) + min(beverage) - 50
print(price)
