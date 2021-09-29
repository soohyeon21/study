# 11399 ATM

# 앞에 사람이 걸리는 시간이 짧아야, 뒤에 있는 사람이 덜 기다린다.
# sort를 해서 오름차순으로 정렬시키자.
# 전체 소요 시간으로 따지자면, 0번째는 n번 만큼, 1번째는 (n-1)번 만큼 반복하여 더해진다.

# sort()말고 sorted()를 사용해 copy본을 만들어 전개하였다.

n = int(input())
pi = list(map(int, input().split()))

pi2 = sorted(pi)

smin = 0

for i in range(n):
    smin += (n - i) * pi2[i]

print(smin)
