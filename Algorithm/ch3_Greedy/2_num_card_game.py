# pg.96 #2 숫자 카드 게임

# 각 행에서 제일 작은 수를 찾고, 그 수 중에서 가장 큰 수를 찾는 코드.

# max(arg1, arg2, arg3, *args)
# max() 괄호 안에 비교 대상이 여러 개 들어가도 됨.
# min()도 마찬가지.

n, m = map(int, input().split())
a = []

for _ in range(n):
    b = list(map(int, input().split()))
    a.append(min(b))
print(max(a))

# 아래와 같이 c에 list()를 중복 사용해도 괜찮음.
##c = list(map(int, input().split()))
##c = list(map(int, input().split()))
##print(c)
