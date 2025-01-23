# 14469

import sys

n = int(sys.stdin.readline())
cowt = sorted([tuple(map(int, sys.stdin.readline().split())) for _ in range(n)], key=lambda x:x[0])

end = 0
for i in range(n):
    if (end < cowt[i][0]):
        end = cowt[i][0] + cowt[i][1] # or max(end, cowt[i][0])
    else:
        end += cowt[i][1] # or if 끝난 후에 공통으로 end += cowt[i][1]

print(end)
