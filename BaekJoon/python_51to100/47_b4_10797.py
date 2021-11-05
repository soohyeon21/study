# 10797

day = int(input())
car = list(map(int, input().split()))

for i in range(5):
    car[i] %= 10

print(car.count(day))
