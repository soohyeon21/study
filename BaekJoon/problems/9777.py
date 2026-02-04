# 9777

import sys

birthm = {i:0 for i in range(1, 13)}

n = int(sys.stdin.readline())
for _ in range(n):
    idn, birth = sys.stdin.readline().split()
    birthm[int(birth.split('/')[1])] += 1

for k, v in birthm.items():
    print(k, v)
