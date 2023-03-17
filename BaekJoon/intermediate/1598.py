# 1598

# 조금 더 짧은 코드로는, 두 수에서 1씩 뺀 다음에 abs(a//4-b//4)+abs(a%4-b%4) 하는 방법도 있다.
# 왜 그런지는 몇가지 경계에 있는 경우로 생각해보면 알 수 있다 호호

import sys

a, b = map(int, sys.stdin.readline().split())

rowa = a % 4 if a%4 != 0 else 4
cola = a//4+1 if a%4 != 0 else a//4
rowb = b % 4 if b%4 != 0 else 4
colb = b//4+1 if b%4 != 0 else b//4

squa = abs(rowa - rowb) + abs(cola-colb)
print(squa)
