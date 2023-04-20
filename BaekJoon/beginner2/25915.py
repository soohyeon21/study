# 25915

# "ILOVEYONSET" 순서대로 입력해야 한다.

import sys

pin = "ILOVEYONSEI"
total = 0
for i in range(1, len(pin)):
    total += abs(ord(pin[i])-ord(pin[i-1]))

now = ord(sys.stdin.readline().rstrip())
total += abs(now - ord(pin[0]))
print(total)
