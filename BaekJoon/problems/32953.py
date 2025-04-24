# 32953

import sys

n, m = map(int, sys.stdin.readline().split())

check = {}
for class_id in range(n):
    k = int(sys.stdin.readline())
    student = list(map(int, sys.stdin.readline().split()))
    for person in student:
        check[person] = check.setdefault(person, [])
        check[person].append(class_id)

cnt = 0
for key, value in check.items():
    if (len(value) >= m):
        cnt += 1

print(cnt)
