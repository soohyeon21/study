# 9286

import sys

n = int(sys.stdin.readline())
for i in range(1, n+1):
    print(f"Case {i}:")
    m = int(sys.stdin.readline())
    cnt = 0
    for _ in range(m):
        grade = int(sys.stdin.readline())
        if (grade < 6):
            print(grade + 1)
