# 34760

import sys

elephant = list(map(int, sys.stdin.readline().split()))

print(max(max(elephant[:-1])+1, elephant[-1]))
