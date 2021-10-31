# 2475

arr = list(map(int, input().split()))

ssum = 0
for val in arr:
    ssum += val**2

print(ssum % 10)
