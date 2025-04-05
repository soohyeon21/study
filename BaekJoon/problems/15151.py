# 15151

import sys

k, d = map(int, sys.stdin.readline().split())

books = 0
while (d >= k):
    d -= k
    books += 1
    k *= 2

print(books)
