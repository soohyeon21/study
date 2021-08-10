# 2884

# 둘 다 맞는 풀이
# (m >= 45)일 때는 h는 전혀 고려 사항이 아니다.
# 등호(=)인 경우를 조심하자.

h, m = map(int, input().split())

if ((h > 0) and (m < 45)):
    h -= 1
    m += 15
elif ((h == 0) and (m < 45)):
    h = 23
    m += 15
elif ((h > 0) and (m >= 45)):
    m -= 45
elif ((h == 0) and (m >= 45)):
    m -= 45
print(h, m)

####
####
####

h, m = map(int, input().split())

if (m < 45):
    m += 15
    if (h > 0):
        h -= 1
    else:
        h = 23
else:
    m -= 45
print(h, m)
