# 6888

import sys

x = int(sys.stdin.readline())
y = int(sys.stdin.readline())

for i in range((y-x)//60+1):
    print(f"All positions change in year {x + i*60}")
