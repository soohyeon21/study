# 15104

# 복잡하게 생각하지 않아도 되는 문제이다.

import sys

s = sys.stdin.readline().rstrip()

isEvenIn = False
for left in range(len(s)-1):
    for right in range(left+1, len(s)):
        if (s[left:right] == s[left:right][::-1]):
            if (len(s[left:right])%2 == 0):
                isEvenIn = True

if (isEvenIn):
    print("Or not.")
else:
    print("Odd.")
