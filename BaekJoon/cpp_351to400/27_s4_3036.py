# 3036

# 분모(denominator), 분자(numerator)

# 유클리드 호제법으로 최대공약수 구하기

# math.gcd() # 최대공약수
# math.lcm() # 최소공배수

import sys

def gcf(a, b):
    while (b != 0):
        num = a % b
        a = b
        b = num
    return a

n = int(sys.stdin.readline())
ring = list(map(int, sys.stdin.readline().split()))

for i in range(1, n):
    gcfnum = gcf(ring[0], ring[i])
    print(f"{ring[0]//gcfnum}/{ring[i]//gcfnum}")
