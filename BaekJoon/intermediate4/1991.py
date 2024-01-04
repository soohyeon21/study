# 1991

# 트리 전위/중위/후위 순회

import sys

def pre_order(root):
    if (root != "."):
        print(root, end="")
        pre_order(tree[root][0])
        pre_order(tree[root][1])

def in_order(root):
    if (root != "."):
        in_order(tree[root][0])
        print(root, end="")
        in_order(tree[root][1])

def post_order(root):
    if (root != "."):
        post_order(tree[root][0])
        post_order(tree[root][1])
        print(root, end="")


n = int(sys.stdin.readline())
tree = {}

for _ in range(n):
    parent, left, right = sys.stdin.readline().split()
    tree[parent] = (left, right)

pre_order("A")
print()
in_order("A")
print()
post_order("A")
