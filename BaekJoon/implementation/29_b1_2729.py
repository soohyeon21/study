# 2729

# format(number, 'b') # 이진수로 앞에 "0b" 없이 출력
# 숫자를 다른 진수의 문자열로 바꿀 때 접두어 제외 가능
# '#b'로 사용하면 접두어 포함 가능

# 내장 함수 bin(), oct(), hex()

import sys

t = int(sys.stdin.readline())
for _ in range(t):
    a, b = sys.stdin.readline().split()
    summ = int(a, 2)+ int(b, 2)
    print(bin(summ)[2:])
