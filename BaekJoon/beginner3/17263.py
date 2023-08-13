# 17263

# 어차피 제일 큰 값이므로 max값을 찾아도 된다.

import sys

n = int(sys.stdin.readline())
a = sorted(list(map(int, sys.stdin.readline().split())))
print(a[-1])
