# 10992

# 간단해 보이는데도 불구하고 쉽게 풀지는 못했다.
# 이런 문제는 for i in range(1, n+1)로, 1부터 시작하는 i로 생각하는게 더 쉬우려나.

# i=1일때를 i=n일때랑 합치든, i!=n일때랑 합치든.
# 정 모르겠으면 i=1,rest,n일때 다 분리하던가.

import sys

n = int(sys.stdin.readline())

for i in range(1, n+1):
    if ((i == 1) or (i == n)):
        print((n-i)*" " + "*"*(2*i-1))
    else:
        print(" "*(n-i) + "*" + " "*(2*(i-1)-1) + "*")
