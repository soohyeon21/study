# 2947

# 어차피 1~5 다섯개 숫자만 있으니까, sort 안쓰고 swood = [1, 2, 3, 4, 5] 이렇게만 설정했어도 충분했다.

import sys

wood = list(map(int, sys.stdin.readline().split()))
swood = sorted(wood)

while (wood != swood):
    for i in range(4):
        if (wood[i] > wood[i+1]):
            wood[i], wood[i+1] = wood[i+1], wood[i]
            print(*wood)
