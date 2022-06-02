# 10864

# 각 학생의 번호를 list의 index로 사용하는 방법도 있댜.

import sys

friend = []

n, m = map(int, sys.stdin.readline().split())
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    friend.append(a)
    friend.append(b)
for i in range(1, n+1):
    print(friend.count(i))
