# 4358

# try-except EOFError가 시간초과 되는 문제였음.

import sys

trees = {}
while (1):
    tree = sys.stdin.readline().rstrip()
    if (tree == ""):
        break
    
    trees[tree] = trees.setdefault(tree, 0)
    trees[tree] += 1

total = sum(map(int, trees.values()))
for name in sorted(list(trees.keys())):
    print(f"{name} {trees[name]/total*100:.4f}")
