# 10093

# input이 오름차순으로 주어지지 않는 경우도 생각해야 한다.

# a, b = b, a하면 바로 뒤바뀐다.

import sys

a, b = map(int, sys.stdin.readline().split())

if (a < b):
    print(b-a-1)
elif (a == b):
    print(0)
else: # a > b
    a, b = b, a
    print(b-a-1)
    
for i in range(a+1, b):
    print(str(i), end=" ")
