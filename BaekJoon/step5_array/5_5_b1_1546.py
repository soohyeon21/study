# 1546

# max(), sum(), list() 사용 or not.

n = int(input())

a = list(map(int, input().split()))
#print(a) #
m = max(a)

for i in range(n):
    a[i] = a[i] / m * 100
#print(a) #
print(sum(a) / n)
