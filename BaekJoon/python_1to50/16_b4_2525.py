# 2525

# 굳이 조건을 나누지 않아도 괜찮지는 않은지 생각해보자
# 나머지 연산 사용

h, m = map(int, input().split())
need = int(input())

m += need

if (m < 60):
    print(h, m)
else: # m >= 60
    plush = m // 60
    m %= 60
    h += plush
    if (h >= 24):
        h -= 24
    print(h, m)

# 맞는 풀이2
##h, m = map(int, input().split())
##need = int(input())
##
##m += need
##
##plush = m // 60
##m %= 60
##h += plush
##h %= 24
##print(h, m)
