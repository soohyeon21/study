# 11094

import sys

n = int(sys.stdin.readline())

for _ in range(n):
    sen = sys.stdin.readline().rstrip()
    if (sen[:10] == "Simon says"):
        print(sen[10:])
