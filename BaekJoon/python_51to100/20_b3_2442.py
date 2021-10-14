# 2442

# format 함수나 center()를 쓸 수 있을 줄 알았는데.
# 이 방법밖에 없나?

n = int(input())

for i in range(1, n * 2, 2):
    aa = ((2*n-1) - i) // 2
    print(" "*aa + "*"*i)
