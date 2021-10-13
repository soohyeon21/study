# 2441

# rjust()라는 것도 있고
# '*'랑 ' ' 갯수만큼 출력하는 방법도 있고

n = int(input())

for i in range(n, 0, -1):
    print("%*s" %(n, '*' * i))
