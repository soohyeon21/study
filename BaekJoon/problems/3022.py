# 3022

# N명의 아이들이 있지만, 모두가 음식을 가져가지는 않을 수 있다.(N개의 목록에 이름이 등장하지 않을 수 있다.)
# ** 경고를 받았더라도, 음식은 가져간다!! **

import sys

n = int(sys.stdin.readline())

food = {}
warn = 0
for _ in range(n):
    name = sys.stdin.readline().rstrip()
    food[name] = food.setdefault(name, 0)

    others = sum(food.values()) - food[name]
    if (others < food[name]):
        warn += 1
    food[name] += 1

print(warn)
