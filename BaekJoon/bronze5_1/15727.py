# 15727

# 1분에 최대 5만큼씩 이동할 수 있다는 말이다.

import sys

l = int(sys.stdin.readline())
t = l//5
if (l%5):
    t += 1
print(t)
