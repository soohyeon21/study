# 1764

import sys

n, m = map(int, sys.stdin.readline().split())
name = []
cnt = [1 for x in range(n)]
sortname = []
for _ in range(n):
    lname = sys.stdin.readline().rstrip()
    name.append(lname)

for i in range(m):
    sname = sys.stdin.readline().rstrip()
    if (sname in name):
        cnt[name.index(sname)] += 1

print(n - cnt.count(1))
for j in range(n):
    if (cnt[j] > 1):
        sortname.append(name[j])
sortname.sort()
print("\n".join(sortname))
