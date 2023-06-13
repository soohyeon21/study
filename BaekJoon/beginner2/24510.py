# 24510

import sys

f = "for"
w = "while"
cnt = 0

c = int(sys.stdin.readline())
for _ in range(c):
    code = sys.stdin.readline().rstrip()
    cnt = max(cnt, code.count(f)+code.count(w))

print(cnt)
