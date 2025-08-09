# 30402

import sys

total = set()
for _ in range(15):
    line = set(sys.stdin.readline().split())
    total.update(line)

if ('w' in total):
    print("chunbae")
elif ("b" in total):
    print('nabi')
elif ('g' in total):
    print('yeongcheol')
