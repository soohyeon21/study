# 2992

# 그냥 each_int가 x보다 큰 경우에만 num_set에 append하고, num_set에서 min값 출력하는 방법도 있다.

import sys
from itertools import permutations

x = sys.stdin.readline().rstrip()
num_set_str = list(permutations([num for num in x], len(x)))
##num_set = [int("".join(each)) for each in num_set_str]
num_set = []
for each in num_set_str:
    each_int = int("".join(each))
    if ((len(str(each_int)) == len(x)) and (each_int not in num_set)):
        num_set.append(each_int)

num_set.sort()
idx = num_set.index(int(x))
if (idx == len(num_set)-1):
    print(0)
else:
    print(num_set[idx+1])
