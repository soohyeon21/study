# 21612

import sys

c = int(sys.stdin.readline())
kpa = 5*c - 400
print(kpa)
if (kpa > 100):
    print(-1)
elif (kpa == 100):
    print(0)
else:
    print(1)
