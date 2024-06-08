# 1235

import sys

n = int(sys.stdin.readline())
pid = [sys.stdin.readline().rstrip() for _ in range(n)]

for k in range(1, len(pid[0])+1):
    k_id = [pid[i][len(pid[0])-k:] for i in range(n)]
    if (len(set(k_id)) == len(k_id)): # or n도 가능
        print(k)
        break
