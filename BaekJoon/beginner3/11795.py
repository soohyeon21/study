# 11795

# 조건을 꼼꼼히 확인하자. "No"가 아니라 "NO"이다.

import sys

t = int(sys.stdin.readline())
setabc = [0, 0, 0]
for _ in range(t):
    abc = list(map(int, sys.stdin.readline().split()))
    for i in range(3):
        setabc[i] += abc[i]
    minset = min(setabc)
    if (minset < 30):
        print("NO")
    else:
        print(minset)
        for j in range(3):
            setabc[j] -= minset
