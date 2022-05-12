# 9093

import sys

t = int(sys.stdin.readline())
for _ in range(t):
    sen = sys.stdin.readline().rstrip().split()
    
    for i in range(len(sen)):
        sen[i] = sen[i][::-1]

    print(" ".join(sen))
