# 25501

# 문제에서 알려준 재귀함수 code 그대로 사용해도 될듯.

import sys

t = int(sys.stdin.readline())
for _ in range(t):
    s = sys.stdin.readline().rstrip()

    isPal = True
    same = 0
    if (len(s)%2 == 0):
        if (s[:len(s)//2][::-1] != s[len(s)//2:]):
            isPal = False
    elif (len(s)%2 != 0):
        if (s[:len(s)//2][::-1] != s[len(s)//2+1:]):
            isPal = False

    if (not isPal):
        for i in range(len(s)//2):
            if (s[i] == s[len(s)-1-i]):
                same += 1
            else:
                break

    if (isPal):
        print(1, len(s)//2+1)
    else:
        print(0, same+1)
