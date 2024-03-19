# 11576

# or python 진법 변환 module 사용하기?
# -> python은 int, bin, oct, hex 등만 지원. 이 방법은 안될듯.

#
# sol1) A진법 -> 10진법 -> B진법
#
import sys

A, B = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline())
numA = list(map(int, sys.stdin.readline().split()))

num10 = 0
for i in range(m):
    num10 += numA[i] * A**(m-1-i)

numB = []
while (num10 != 0):
    digit = num10 % B
    numB.insert(0, digit)
    num10 //= B

print(*numB)
