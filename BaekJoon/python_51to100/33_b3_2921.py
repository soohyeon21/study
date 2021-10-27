# 2921

# for문 두 번 사용하는 방법도 있기는 하다.

def count_n(n):
    lower = n*(n+1)
    upper = n*(n+1)//2
    return (lower + upper)

n = int(input())

val = 0
for i in range(1, n+1):
    val += count_n(i)

print(val)
