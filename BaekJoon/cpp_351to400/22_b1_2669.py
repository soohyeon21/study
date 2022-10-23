# 2669

# 크으... 졸업 프로젝트가 떠오르는 코드군.
# 그나저나 그때 도움 되었던 문제가 뭐였더라... 이거랑 비슷했는데.

# 101x101의 이중 list를 사용하는 방법도 있지만, list에 좌표를 넣고 len(set(list)) 방법도 있다.

# plane = [[0] * 101] * 101 # 문제 생긴다. 아마 값을 복사해서 늘리는 방식인듯.

import sys

plane = [[0 for aa in range(101)] for bb in range(101)]
for _ in range(4):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    for y in range(y1, y2):
        for x in range(x1, x2):
            plane[y][x] = 1

cnt = 0
for i in range(101):
    cnt += plane[i].count(1)

print(cnt)
