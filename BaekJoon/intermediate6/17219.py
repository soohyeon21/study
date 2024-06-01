# 17219

import sys

n, m = map(int, sys.stdin.readline().split())

password = {}
for _ in range(n):
    site, pw = sys.stdin.readline().split()
    password[site] = pw

for i in range(m):
    find_site = sys.stdin.readline().rstrip()
    print(password[find_site])
