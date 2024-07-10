# 9339

# 6시간 이하를 ([h, m]<[6, 1])으로도 판단할 수 있다.
# [5, 35]<[6, 1] # True

import sys

t = int(sys.stdin.readline())
for _ in range(t):
    k = int(sys.stdin.readline())
    students_id = list(map(int, sys.stdin.readline().split()))

    n = int(sys.stdin.readline())
    records = {}
    for i in range(n):
        pid, h, m = map(int, sys.stdin.readline().split())
        records[pid] = h*60 + m

    clear = 0
    congrat = []
    for student in students_id:
        if (0 <= records[student] <= 6*60):
            clear += 1
            congrat.append((student, records[student]))

    congrat.sort(key = lambda x:x[1])

    print(congrat[0][0], clear)
