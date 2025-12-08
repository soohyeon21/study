# 32399

# 두번째와 세번째 조건을 서로 바꾸면 코드를 더 줄일 수 있을 듯!

import sys

s = sys.stdin.readline().rstrip()

if (s == '(1)'):
    print(0)
elif (('(1' in s) or ('()' in s) or ('1)' in s)):
    print(1)
else:
    print(2)
