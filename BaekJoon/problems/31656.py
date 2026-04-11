# 31656

import sys

msg = sys.stdin.readline().replace('\n', '') + '#'

before = msg[0]
rst = ''
for i in range(1, len(msg)):
    if (msg[i] != before):
        rst += before
        before = msg[i]

print(rst)
