# 5354

import sys

def printJ(num):
    for row in range(num):
        for col in range(num):
            if (row in [0, num-1]):
                print('#', end='')
            elif (col in [0, num-1]):
                print('#', end='')
            else:
                print('J', end='')
        print()
    print()


t = int(sys.stdin.readline())

for _ in range(t):
    j = int(sys.stdin.readline())
    printJ(j)
