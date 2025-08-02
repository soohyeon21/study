# 21756

# arr=arr[1::2] # idx 1부터 시작해서 2칸씩 건너뜀.

import sys
import math

n = int(sys.stdin.readline())

print(2**int(math.log(n, 2)))
