# 2154

# str()로 더하는 방법 말고, ''.join() 방법도 있다.

import sys

n = int(sys.stdin.readline())

newn = ''
for i in range(1, n+1):
    newn += str(i)

print(newn.find(str(n))+1)
