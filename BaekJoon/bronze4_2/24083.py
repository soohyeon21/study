# 24083

# 시침이 A를 가리킬 때, B 시간이 지난 뒤 가리키는 시침을 구하라.

import sys

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())

after = (a+b)%12
if (after == 0):
    print(12)
else:
    print(after)
