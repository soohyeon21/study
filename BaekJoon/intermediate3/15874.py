# 15874

import sys

k, s = map(int, sys.stdin.readline().split())
plain = sys.stdin.readline().replace("\n", "")

cypher = ""
for letter in plain:
    isCapital = True if letter.isupper() else False
    if (64 < ord(letter.upper()) < 91):
        tmp = chr((ord(letter.upper())-65-26+k)%26+65)
        if (isCapital):
            cypher += tmp.upper()
        else:
            cypher += tmp.lower()
    else:
        cypher += letter

print(cypher)
