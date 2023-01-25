# 3733

# 간만에 EOFError를 써보고 싶었는데... 이런.

import sys

while (1):
    try:
        n, s = map(int, sys.stdin.readline().split())
        print(s//(n+1))
    except:
        break
