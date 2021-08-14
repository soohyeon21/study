# 10818

# len(a) 대신 n 써도 되고.
# sort() # list 정렬
# sort(reverse=True) # list 정렬 역순으로
# reverse() # 단순 list 역으로 정렬

n = int(input())

a = list(map(int, input().split()))
a.sort()
print(a[0], a[(len(a) - 1)])
