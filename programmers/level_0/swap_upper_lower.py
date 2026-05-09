# 대소문자 바꿔서 출력하기

import sys

eng = sys.stdin.readline().rstrip()

result = ''
for letter in eng:
    if (letter.islower()):
        result += letter.upper()
    else:
        result += letter.lower()

print(result)
