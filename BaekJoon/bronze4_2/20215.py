# 20215

import sys

w, h = map(int, sys.stdin.readline().split())
dia = (w**2 + h**2)**0.5

print(w+h-dia)
