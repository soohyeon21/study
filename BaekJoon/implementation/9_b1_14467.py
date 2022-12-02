# 14467

import sys

n = int(sys.stdin.readline())
dic = {}
cnt = 0
for _ in range(n):
    cow, lr = map(int, sys.stdin.readline().split())
    if (cow not in dic):
        dic[cow] = lr
    else:
        if (dic[cow] != lr):
            cnt += 1
            dic[cow] = lr
print(cnt)
