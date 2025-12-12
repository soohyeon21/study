# 14624

# '*'로 끝난 다음에는 공백이 있어서는 안된다.

import sys

n = int(sys.stdin.readline())

if (n%2 == 0):
    print("I LOVE CBNU")
else:
    print("*"*n)
    print(' '*(n//2) + '*')
    for i in reversed(range(n//2)):
        half = ' '*i + '*'
        full = half + ' '*(n//2-1-i)+' '+' '*(n//2-1-i)+ half[::-1]
        print(full.rstrip())
