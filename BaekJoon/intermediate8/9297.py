# 9297

import sys

t = int(sys.stdin.readline())
for idx in range(1, t+1):
    num, den = map(int, sys.stdin.readline().split())
    
    print(f"Case {idx}:", end=' ')
    
    if ((num//den == 0) and (num%den == 0)):
        print(0, end=" ")
    if (num//den != 0):
        print(num//den, end=" ")
    if (num%den != 0):
        print(f"{num%den}/{den}", end="")
    print()
