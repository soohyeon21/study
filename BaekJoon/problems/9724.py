# 9724

# 참고로, 1259**3=1,995,616,979, 1260**3=2,000,376,000

# math.sqrt(), math.cbrt()

import sys
import math

t = int(sys.stdin.readline())
for idx in range(1, t+1):
    a, b = map(int, sys.stdin.readline().split())
    rst = math.ceil(int(math.cbrt(b)) - math.cbrt(a))
    if (math.cbrt(a) == int(math.cbrt(a))):
        rst += 1
    
    print(f"Case #{idx}: {rst}")
