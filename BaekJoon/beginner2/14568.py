# 14568

# 택희 2b개, 영훈이 a+2+c개, 남규 a개
# 단, a>0, b>0, c>=0

import sys

n = int(sys.stdin.readline())

cnt = 0
for a in range(1, (n-4)//2+1):
    for b in range(1, (n-4)//2+1):
        for c in range(n-5):
            if (2*a + 2*b + c + 2 == n):
                cnt += 1
print(cnt)
