# 1978
# 2nd try

import sys

n = int(sys.stdin.readline())
nums = [1 for _ in range(1001)]
nums[0], nums[1] = 0, 0

for i in range(2, int(1000**0.5)+2):
    for j in range(2, 1000//i+1):
        nums[i*j] = 0

check = list(map(int, sys.stdin.readline().split()))
cnt = 0
for c in check:
    if (nums[c] == 1):
        cnt += 1

print(cnt)
