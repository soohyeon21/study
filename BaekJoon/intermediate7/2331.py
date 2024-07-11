# 2331

import sys

a, p = map(int, sys.stdin.readline().split())

d = [-1, a]
end = 0
while (1):
    after = sum(int(digit)**p for digit in str(d[-1]))
    if (after not in d):
        d.append(after)
    else:
        end = d.index(after)
        break

print(len(d[1:end]))
