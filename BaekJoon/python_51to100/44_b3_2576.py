# 2576

# if (number): # number에 element가 있으면

import sys

number = []
for _ in range(7):
    num = int(sys.stdin.readline())
    if (num % 2 != 0): # odd
        number.append(num)

if (len(number) == 0):
    print(-1)
    
else:
    print(sum(number))
    print(min(number))
