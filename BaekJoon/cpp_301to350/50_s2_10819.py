# 10819

# 10974번의 '모든 순열' 문제는 1~N까지의 N개의 수로, 수의 중복이 일어나지 않는다.
# 그러나 본 문제의 경우, 중복되는 숫자가 존재할 수 있다.
# 따라서 if와 not in을 사용하여 해당 숫자가 사용되었는지 판단하면 안되고,
# 값만 같은 수가 아니라 바로 '그' 숫자가 사용되었는지를 판단할 필요가 있다.
# 따라서 j index와 check list를 사용할 것.

import sys

def dfs():
    if (len(tmp) == n):
        total = 0
        for i in range(n-1):
            total += abs(tmp[i] - tmp[i+1])
        rst.append(total)

    for j in range(n):
        if (not check[j]):
            tmp.append(lst[j])
            check[j] = 1
            dfs()
            tmp.pop()
            check[j] = 0

n = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
tmp = []
rst = []
check = [0 for x in range(n)]
dfs()
print(max(rst))
