# 5576

# sort(reverse=True)
# sorted(reverse=True)

import sys

w = []
for _ in range(10):
    w.append(int(sys.stdin.readline()))

k = [int(sys.stdin.readline()) for i in range(10)]

w1 = sorted(w, reverse=True)
k.sort(reverse=True)

print(sum(w1[:3]), sum(k[:3]))
