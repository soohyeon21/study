# 3049

# 규칙만 알면 매우 간단하다.

# 대각선의 교차점을 사각형의 두 대각선의 교차점이라 생각하면,
# 결국에는 볼록 다각형에서 4각형의 개수를 찾는 문제와 동일하다.
# 즉, nC4 = n(n-1)(n-2)(n-3)/4!

import sys

n = int(sys.stdin.readline())
num = n*(n-1)*(n-2)*(n-3)//24
print(num)