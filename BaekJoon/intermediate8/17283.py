# 17283

import sys

l = int(sys.stdin.readline())
r = int(sys.stdin.readline())

tree = [l]
branch = l
while (1):
    branch = int(tree[-1] * r/100)
    if (branch <= 5):
        break
    tree.append(branch)

height = sum(tree[i]*2**i for i in range(1, len(tree)))

print(height)
