# 13987

# 전체 경우의 수 36에서 무승부인 경우를 제외한 수로 나눠줘야 함.

import sys

first = list(map(int, sys.stdin.readline().split()))
second = list(map(int, sys.stdin.readline().split()))

fwin = 0
same = 0
for i in range(6):
    for j in range(6):
        if (first[i] > second[j]):
            fwin += 1
        if (first[i] == second[j]):
            same += 1

print(f"{round(fwin/(36-same), 5):.5f}")
