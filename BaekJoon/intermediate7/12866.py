# 12866

import sys

l = int(sys.stdin.readline())
s = sys.stdin.readline().rstrip()

total = 1
for letter in "ACGT":
    total *= s.count(letter)

print(total%1000000007)
