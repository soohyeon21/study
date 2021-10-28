# 10995

# 조금 더 쉽게 생각해보자.

n = int(input())

arr1 = '*'
arr2 = ' *'

for i in range(1, n):
    if (n == 1):
        arr1 = "*"
    else:
        arr1 += " *"
        arr2 += " *"

if (n == 1):
    print(arr1)
else:
    for j in range(1, n+1):
        if (j % 2 == 1):
            print(arr1)
        else:
            print(arr2)
