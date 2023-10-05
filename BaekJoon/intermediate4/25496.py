# 25496

# while 사용시 n개보다 많은 장신구 제작하지 않도록 주의
# while과 for 모두 사용 가능하고 큰 차이 없다면 for 사용하도록 하자.

import sys

p, n = map(int, sys.stdin.readline().split())
a = sorted(list(map(int, sys.stdin.readline().split())))

cnt = 0

# sol1) while
while ((p < 200) and (cnt < n)):
    p += a[cnt]
    cnt += 1

# sol2) for
##for i in range(n):
##    if (p < 200):
##        p += a[cnt]
##        cnt += 1
##    else:
##        break

print(cnt)
