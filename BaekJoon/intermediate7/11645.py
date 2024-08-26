# 11645

import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    
    visited = set()
    for times in range(n):
        city = sys.stdin.readline().rstrip()
        visited.add(city)
        
    print(len(visited))
