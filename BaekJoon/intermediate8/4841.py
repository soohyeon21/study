# 4841

import sys

t = int(sys.stdin.readline())
for _ in range(t):
    num = sys.stdin.readline().rstrip()+"#"

    prev = num[0]
    cnt = 1
    result = ""
    for i in range(1, len(num)):
        if (prev != num[i]):
            result += str(cnt)+prev
            prev = num[i]
            cnt = 1
        else:
            cnt += 1

    print(result)
