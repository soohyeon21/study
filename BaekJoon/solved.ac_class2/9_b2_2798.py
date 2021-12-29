# 2798

# 그냥 애초에 m보다 큰 값은 append 안하면 된다.

# from itertools import combinations
# for elements in combinations(list, number):

# 이런 식으로 combination도 사용 가능.

import sys

n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

summ = []
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            value = arr[i] + arr[j] + arr[k]
            if (value > m):
                continue
            else:
                summ.append(value)
print(max(summ))

# 크지 않은 수를 뽑겠다는 내 노력...
#
##summ.append(m)
##narr = sorted(summ)
##
##fd = narr[narr.index(m) + 1]
##if (fd == m):
##    print(m)
##else:
##    print(narr[narr.index(m) - 1])
