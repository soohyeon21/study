# 2460

import sys

many = []
train = 0
for _ in range(10):
    Out, In = map(int, sys.stdin.readline().split())
    train += (In - Out)
    many.append(train)

print(max(many))
    
