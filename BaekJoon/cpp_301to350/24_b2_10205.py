# 10205

# "입력은 히드라의 머리를 모두 제거했다면 더 이상의 행동은 없도록 주어진다."
# h==0일때의 경우는 고려하지 않아도 된다는 말이었다.

import sys

k = int(sys.stdin.readline())

for i in range(1, k+1):
    h = int(sys.stdin.readline())
    work = sys.stdin.readline().rstrip()
    for w in work:
        if (h == 0):
            break
        elif (w == "c"):
            h += 1
        else:
            h -= 1
    print(f"Data Set {i}:\n{h}\n")
