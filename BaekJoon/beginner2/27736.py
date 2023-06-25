# 27736

import sys

n = int(sys.stdin.readline())
vote = list(map(int, sys.stdin.readline().split()))

result = ""
if (vote.count(0) >= n/2):
    result = "INVALID"
elif (sum(vote) > 0):
    result = "APPROVED"
else:
    result = "REJECTED"

print(result)
