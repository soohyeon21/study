# 11047 동전 0

# 동전의 액수는 배수 관계에 있다.
# 큰 수 부터 차례로 나눠주면 된다.

# list.sort(reverse=True)
# list2 = sorted(list, reverse=True)

# 어차피 for문 돌릴거면, 굳이 index를 찾으려고 한 번 더 for문을 쓸 필요는 없는 것 같다.

n, k = map(int, input().split())

coin = []
for _ in range(n):
    coin.append(int(input()))
cor = sorted(coin, reverse=True)

for value in cor:
    if (value < k):
        stand = cor.index(value)
        break

cnt = 0
for i in range(stand, len(cor)):
    cnt += k // cor[i]
    k %= cor[i]
print(cnt)
