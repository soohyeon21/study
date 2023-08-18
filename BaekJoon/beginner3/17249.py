# 17249

# "(^0^)" 또는 "0"을 기준으로 split() 하는 방법도 있다.

import sys

tb = sys.stdin.readline().rstrip()
zero = tb.index("0")
left = tb[:zero].count("@")
right = tb[zero:].count("@")
print(left, right)
