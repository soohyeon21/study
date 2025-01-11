# 21633

import sys

k = int(sys.stdin.readline())

comm = min(max(100, 25+k*0.01), 2000)
print(f"{comm:.2f}")
