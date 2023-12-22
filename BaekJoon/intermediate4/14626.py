# 14626

# *을 찾아내는 부분에서 0~9까지 * 위치에 대입해보면서 찾는 방법으로 풀어야 한다.
# 방정식 풀듯 *만 남기고 풀면 안됨. modular 연산은 분배법칙이 안된다나.

import sys

isbn = sys.stdin.readline().rstrip()
table = [1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1]
target = 0
total = 0
for i in range(12):
    if (isbn[i].isdigit()):
        total += int(isbn[i])*table[i]
    else:
        target = i

for k in range(10):
    if ((total + k*table[target] + int(isbn[-1]))%10 == 0):
        print(k)
        break
