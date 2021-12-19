# 11655

import sys

inword = sys.stdin.readline().rstrip()
prnt = ""

for letter in inword:
    # small letter
    if (97 <= ord(letter) <= 109):
        prnt += chr(ord(letter) + 13)
    elif (110 <= ord(letter) <= 122):
        prnt += chr(ord(letter) - 13)
    # capital letter
    elif (65 <= ord(letter) <= 77):
        prnt += chr(ord(letter) + 13)
    elif (78 <= ord(letter) <= 90):
        prnt += chr(ord(letter) - 13)
    else:
        prnt += letter
print(prnt)
