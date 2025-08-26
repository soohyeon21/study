# 31432

# 0~9까지의 모든 수는 x111을 하면 소수가 아닌 수가 된다.
# 0과 1도 소수가 아닌 수이다.

import sys

n = int(sys.stdin.readline())
d = list(map(int, sys.stdin.readline().split()))

print("YES")
if (0 in d):
    print(0)
elif (1 in d):
    print(1)
else:
    print(int(str(d[0])*2))
