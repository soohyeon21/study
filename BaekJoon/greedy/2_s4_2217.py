# 2217 로프

# 가능한 무게 수를 계산할 때, 전의 원소와 비교하여 큰 수일 때만 append 하는 방법도 있다.

n = int(input())
weight = []
tol = []

for _ in range(n):
    weight.append(int(input()))
    
weight.sort()

for i in range(n):
    tol.append(weight[0] * (n - i))
    weight.remove(weight[0])
    
print(max(tol))
