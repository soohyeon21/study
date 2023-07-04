# 3076

# 후훗 xd 생각한건 좀 잘한듯!

import sys

r, c = map(int, sys.stdin.readline().split())
a, b = map(int, sys.stdin.readline().split())

xd = ["X", "."]
chess = []
for rr in range(r):
    line = ""
    for cc in range(c):
        line += xd[(rr%2+cc%2)%2]*b
    for aa in range(a):
        chess.append(line)

print("\n".join(chess))
##print(*chess, sep="\n")
