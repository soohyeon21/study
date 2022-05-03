# 8949

# ''.join(list_name)

import sys

A, B = sys.stdin.readline().split()
a = list(A)[::-1]
b = list(B)[::-1]

if (len(a) >= len(b)):
    for k in range(len(a) - len(b)):
        b.append("0")
else:
    for k in range(len(b) - len(a)):
        a.append("0")

c = []
for i in range(len(a)):
    c.append(str(int(a[i]) + int(b[i])))

c = c[::-1]
print("".join(c))
