# 9971

# dictionary나 "ABC...XYZVWX...STU" 문자열 사용하는 방법도 있음.

import sys

while (1):
    first = sys.stdin.readline().rstrip()
    if (first == "ENDOFINPUT"):
        break

    sent = sys.stdin.readline().rstrip()
    nsent = ""
    for letter in sent:
        if (letter.isalpha()):
            #nsent += chr(ord(letter)+21) if 65<=ord(letter)<=69 else chr(ord(letter)+21-26)
            nsent += chr((ord(letter)-70)%26 + 65)
        else:
            nsent += letter
    end = sys.stdin.readline().rstrip()
    print(nsent)
