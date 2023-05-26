# 16018

import sys

n = int(sys.stdin.readline())
yester = sys.stdin.readline().rstrip()
today = sys.stdin.readline().rstrip()

cnt = 0
for i in range(len(today)):
    if ((yester[i] == "C") and (today[i] == "C")):
        cnt += 1
print(cnt)
