# 16199

# 조금 더 깔끔하게 푸는 방법이 있을 듯도??

import sys

birth = list(map(int, sys.stdin.readline().split()))
now = list(map(int, sys.stdin.readline().split()))

# man
old = now[0] - birth[0]
if (now[1] == birth[1]):
    if (now[2] < birth[2]):
        old -= 1
elif (now[1] < birth[1]):
    old -= 1
elif (now[1] > birth[1]):
    pass

# se
old2 = now[0] - birth[0] + 1

# yeon
old3 = now[0] - birth[0]

print(old)
print(old2)
print(old3)
