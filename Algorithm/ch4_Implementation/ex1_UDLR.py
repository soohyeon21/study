# 예제 4-1 상하좌우

# input().split()은 list(input().split())과 같다. 동일하게 list로 만들어 준다.

n = int(input())
plan = input().split()
##plan = list(input().split())

x, y = 1, 1
for dire in plan:
    if ((dire == "U") and (1 < x)):
        x -= 1
    elif ((dire == "D") and (x < n)):
        x += 1
    elif ((dire == "L") and (1 < y)):
        y -= 1
    elif ((dire == "R") and (y < n)):
        y += 1
print(x, y)
