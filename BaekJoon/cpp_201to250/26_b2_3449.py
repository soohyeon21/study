# 3449

import sys

t = int(sys.stdin.readline())

for _ in range(t):
    t1 = sys.stdin.readline().rstrip()
    t2 = sys.stdin.readline().rstrip()
    cnt = 0
    for i in range(len(t1)):
        if (t1[i] != t2[i]):
            cnt += 1
    print("Hamming distance is %d." %(cnt))
