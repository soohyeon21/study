# 16171

# isdigit() # 문자열인데, 숫자이면 True, 문자이면 False

import sys

s = sys.stdin.readline().rstrip()
k = sys.stdin.readline().rstrip()
real = ""

for letter in s:
    if (48 <= ord(letter) <= 57):
        pass
    else:
        real += letter

if (k in real):
    print(1)
else:
    print(0)
