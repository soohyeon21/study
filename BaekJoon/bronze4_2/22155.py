# 22155

# (i<=1 이고 f<=2) 이거나 (i<=2 이고 f<=1) 이면 Yes, 아니면 No 출력

import sys

t = int(sys.stdin.readline())

for _ in range(t):
    i, f = map(int, sys.stdin.readline().split())
    if (((i <= 1) and (f <= 2)) or ((i <= 2) and (f <= 1))):
        print("Yes")
    else:
        print("No")
