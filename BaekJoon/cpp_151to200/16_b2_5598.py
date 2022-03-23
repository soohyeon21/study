# 5598

import sys

cword = sys.stdin.readline().rstrip()

oword = ""
for letter in cword:
    ordlt = ord(letter)
    if (68 <= ordlt):
        oword += chr(ordlt - 3)
    else:
        oword += chr(ordlt + 23)
print(oword)
