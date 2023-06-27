# 27512

# 어떤수 & 1 # 어떤수가 짝수이면 0 return, 홀수이면 1 return # 이진수 연산

# 8 & 10 # 8
# 8 and 10 # 10

import sys

n, m = map(int, sys.stdin.readline().split())
if (n*m%2 == 0):
    print(n*m)
else:
    print(n*m-1)
