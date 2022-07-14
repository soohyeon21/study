# 11536

import sys

n = int(sys.stdin.readline())
name = []
for _ in range(n):
    name.append(sys.stdin.readline().rstrip())

asname = sorted(name)
dename = sorted(name, reverse=True)

if (name == asname):
    print("INCREASING")
elif (name == dename):
    print("DECREASING")
else:
    print("NEITHER")
