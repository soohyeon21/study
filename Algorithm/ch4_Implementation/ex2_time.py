# pg.113 #예제4-2 시각

n = int(input())

if (0 <= n < 3):
    print(1575 * n)
elif (3 <= n < 13):
    print(1575 * n + 3600)
elif (13 <= n < 23):
    print(1575 * n + 3600 * 2)
else: # (n == 23)
    print(1575 * n + 3600 * 3)
