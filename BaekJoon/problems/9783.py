# 9783

# islower(), isupper()는 기본적으로 알파벳에 대한 함수이니, isalpha()는 생략해도 됨.

import sys

msg = sys.stdin.readline().replace('\n', '')

enc = ''
for letter in msg:
    if (letter.isalpha()):
        if (letter.islower()):
            enc += str(ord(letter)-96).zfill(2)
        elif (letter.isupper()):
            enc += str(ord(letter)-38).zfill(2)
    elif (letter.isdigit()):
        enc += '#'+letter
    else:
        enc += letter

print(enc)
