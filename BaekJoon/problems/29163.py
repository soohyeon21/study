# 29163

import sys

n = int(sys.stdin.readline())
door = list(map(int, sys.stdin.readline().split()))

odd_cnt, even_cnt = 0, 0
for each in door:
    if (each%2 == 0):
        even_cnt += 1
    else:
        odd_cnt += 1

if (even_cnt > odd_cnt):
    print("Happy")
else:
    print("Sad")
