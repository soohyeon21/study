# 2902

# split('-')을 해서 구분된 단어의 첫 글자만 end=''로 출력하는 방법도 있다.

import sys

al_name = sys.stdin.readline()

short = '' # short = ""로 해도 시간은 68ms로 동일
for letter in al_name:
    if (letter.isupper()):
        short += letter

print(short)
