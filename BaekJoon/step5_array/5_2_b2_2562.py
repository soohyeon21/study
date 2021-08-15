# 2562

# max(리스트명)
# 리스트.index() => 0부터 해서 몇번째 출력.

a = []
for i in range(9):
    a.append(int(input()))

print(max(a))
print(a.index(max(a)) + 1)
