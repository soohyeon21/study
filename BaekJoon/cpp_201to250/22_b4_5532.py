# 5532

# list = [int(input()) for _ in range(5)]

# a.append(d[i] // d[i+2] + 1 if d[i] % d[i+2] else d[i] // d[i+2])

import sys
from math import ceil

days = []
for _ in range(5):
    days.append(int(sys.stdin.readline()))

korean = ceil(days[1]/days[3])
mathe = ceil(days[2]/days[4])
print(days[0] - max(korean, mathe))
