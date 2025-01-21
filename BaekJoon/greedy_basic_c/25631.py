# 25631

# max(mat)은 10**9이기 때문에 min(mat)~max(mat)을 range로 하면 시간초과 발생.

import sys

n = int(sys.stdin.readline())
mat = sorted(list(map(int, sys.stdin.readline().split())))

count_mat = [mat.count(i) for i in mat]
print(max(count_mat))
