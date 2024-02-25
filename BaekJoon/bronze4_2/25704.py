# 25704

import sys

n = int(sys.stdin.readline())
p = int(sys.stdin.readline())

min_price = p # 50000이면 안된다.
if (n >= 5):
    min_price = min(min_price, p-500)
if (n >= 10):
    min_price = min(min_price, p*0.9)
if (n >= 15):
    min_price = min(min_price, p-2000)
if (n >= 20):
    min_price = min(min_price, p*0.75)

print(int(max(0, min_price)))
