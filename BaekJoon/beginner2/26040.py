# 26040

import sys

a = sys.stdin.readline().rstrip()
b = sys.stdin.readline().split()

for upletter in b:
    a = a.replace(upletter, upletter.lower())

print(a)
