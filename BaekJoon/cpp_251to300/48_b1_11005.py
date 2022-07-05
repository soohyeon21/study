# 11005

import sys

n, b = map(int, sys.stdin.readline().split())
jin = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

rst = ""
while (n != 0):
    rst = jin[n%b] + rst
    n //= b

print(rst)
