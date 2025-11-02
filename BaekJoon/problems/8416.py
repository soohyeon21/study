# 8416

# or %10 활용

import sys

a, b = map(int, sys.stdin.readline().split())

end = []

one = 1
for i in range(b):
    one = int(str(one*a)[-1])
    if (one not in end):
        end.append(one)
    else:
        break

remain = b%len(end)

print(end[remain-1])
