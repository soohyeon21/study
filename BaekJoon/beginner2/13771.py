# 13771

# format 함수 사용할 때 float 쓰고 싶으면 f 명시 필수!! 안그럼 default d!!

import sys

n = int(sys.stdin.readline())
price = [0 for x in range(n)]
for i in range(n):
    price[i] = float(sys.stdin.readline())

price.sort()
print(f"{price[1]:.2f}")
#print("%.2f" %price[1])
