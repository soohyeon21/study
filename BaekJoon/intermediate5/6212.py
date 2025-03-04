# 6212

# dict 말고 list 써도 되긴 한다.

# dramatic하게 시간을 줄일 수 있는 방법이 있긴 한데... (제출 번호 87680428)

import sys

m, n = map(int, sys.stdin.readline().split())

digit = {i:0 for i in range(10)}
for num in range(m, n+1):
    for one in str(num):
        digit[int(one)] += 1

print(*digit.values(), sep=' ')
