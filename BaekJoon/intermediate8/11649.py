# 11649

import sys

n = int(sys.stdin.readline())
word = sorted([sys.stdin.readline().rstrip()[::-1] for _ in range(n)])

print(*word, sep='\n')
