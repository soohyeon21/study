# 18005

# 2가 나오는 경우는 n이 4의 배수일 때

import sys

n = int(sys.stdin.readline())

if (n%2 == 1):
    print(0)
elif ((n//2)%2 == 0):
    print(2)
else:
    print(1)
