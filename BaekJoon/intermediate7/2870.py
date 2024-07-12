# 2870

import sys

n = int(sys.stdin.readline())
paper = [sys.stdin.readline().rstrip() for _ in range(n)]

numbers = []
for line in paper:
    filtered = " ".join(line.split(chr(97)))
    for i in range(98, 123):
        filtered = " ".join(filtered.split(chr(i)))
    numbers += list(map(int, filtered.split()))
numbers.sort()
print(*numbers, sep="\n")
