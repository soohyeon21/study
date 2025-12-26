# 35005

# 시계의 모든 숫자는 (h-1), (m-1)의 제한이 있다.
# 중복되는 시간은 제거한다.

import sys

h, m = map(int, sys.stdin.readline().split())

lucky = set()
for s1 in range(10):
    if ((int(str(s1)+'2') <= h-1) and (39 <= m-1)):
        lucky.add(str(s1)+'239')

for s2 in [0, 2, 3]:
    if ((int('2'+str(s2)) <= h-1) and (39 <= m-1)):
        lucky.add('2'+str(s2)+'39')

for s3 in [0, 3, 9]:
    if ((int(str(s3)+'9') <= m-1) and (23 <= h-1)):
        lucky.add('23'+str(s3)+'9')

for s4 in range(10):
    if ((int('9'+str(s4)) <= m-1) and (23 <= h-1)):
        lucky.add('239'+str(s4))

print(len(lucky))
