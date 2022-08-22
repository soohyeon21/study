# 9012

# 오, 두번째 예제 없었으면 틀렸을뻔.

import sys

t = int(sys.stdin.readline())
for _ in range(t):
    bracket = sys.stdin.readline().rstrip()
    val = 0
    for single in bracket:
        if (single == "("):
            val += 1
        else:
            val -= 1
        if (val < 0):
            break
    if (val == 0):
        print("YES")
    else:
        print("NO")
