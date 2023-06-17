# 25630

# 사실 decide가 n//2이어도 상관없다.

import sys

n = int(sys.stdin.readline())
st = sys.stdin.readline().rstrip()

cnt = 0
#decide = n//2+1 if (n%2!=0) else n//2
decide = n//2
for i in range(decide):
    if (st[i] != st[n-i-1]):
        cnt += 1

print(cnt)
