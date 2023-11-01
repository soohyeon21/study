# 9933

import sys

n = int(sys.stdin.readline())
password = [sys.stdin.readline().rstrip() for x in range(n)]

answer = ""
for pw in password:
    if (pw[::-1] in password):
        answer = pw

print(len(answer), answer[len(answer)//2])
