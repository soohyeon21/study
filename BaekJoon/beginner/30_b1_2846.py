# 2846

# 푸는 방법은 다양한 듯.

import sys

n = int(sys.stdin.readline())
p = list(map(int, sys.stdin.readline().split()))
subsum = []

init = 0
end = 0
for i in range(n):
    if (init == 0): # 처음에만
        init = p[i]
    elif (p[i] <= end):
        subsum.append(end - init)
        init = p[i]
    end = p[i]
    if ((i == n-1) and (init != end)):
        subsum.append(end - init)

# print(subsum)
if ((len(subsum) == 0) or (len(subsum) - p.count(0) == 0)):
    print(0)
else:
    print(max(subsum))
