# 13211

# stolen을 set()으로 설정하는 방법도 있다. 이러면 try-except 안써줘도 됨.

# stolen을 list()로 하면 시간초과.

# containment 확인
# set  : O(1)
# dict : O(1)
# list : O(n)

import sys

n = int(sys.stdin.readline())
stolen = {sys.stdin.readline().rstrip():1 for _ in range(n)}

m = int(sys.stdin.readline())

cnt = 0
for i in range(m):
    check = sys.stdin.readline().rstrip()
    try:
        if (stolen[check]):
            cnt += 1
    except:
        pass

print(cnt)
