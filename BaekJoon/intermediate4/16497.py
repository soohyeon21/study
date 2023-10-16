# 16497

# 반납 당일에는 이미 반납을 완료해서 대출가능하다고 생각하고 range(b, r+1) 말고 range(b, r)로 하면 된다.

import sys

n = int(sys.stdin.readline())
date = [0 for x in range(32)]
for _ in range(n):
    b, r = map(int, sys.stdin.readline().split())
    for occupied in range(b, r): # not r+1
        date[occupied] += 1
k = int(sys.stdin.readline())

if (max(date) > k):
    print(0)
else:
    print(1)
