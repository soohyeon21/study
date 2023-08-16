# 17202

# 후훗

import sys

a = sys.stdin.readline().rstrip()
b = sys.stdin.readline().rstrip()
start = "".join(a[i]+b[i] for i in range(8))

for _ in range(14):
    new = ""
    for j in range(len(start)-1):
        new += str(int(start[j])+int(start[j+1]))[-1]
    start = new

print(start)
