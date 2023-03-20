# 2851

import sys

mario = 0
for _ in range(10):
    mush = int(sys.stdin.readline())
    if (abs((mario+mush) - 100) <= abs(mario - 100)):
        mario += mush
    else:
        break

print(mario)
