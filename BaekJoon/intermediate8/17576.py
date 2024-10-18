# 17576

import sys

string = sys.stdin.readline().rstrip()
n = int(sys.stdin.readline())

totals = 0
length = 0
for _ in range(n):
    start, length = map(int, sys.stdin.readline().split())
    totals += start

print(string[totals:totals+length])
