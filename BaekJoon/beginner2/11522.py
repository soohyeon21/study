# 11522

import sys

p = int(sys.stdin.readline())
for _ in range(p):
    k, n = map(int, sys.stdin.readline().split())
    
    s1 = n*(n+1)//2 # n까지의 모든 양수의 합
    s2 = n**2 # n까지의 모든 홀수의 합
    s3 = n*(n+1) # n까지의 모든 짝수의 합

    print(k, s1, s2, s3)
