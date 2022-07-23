# 7600

# if문 안에서 letter not in sen2도 추가했으면 set 안쓰고 할 수 있다.

import sys

while (1):
    sen = sys.stdin.readline().rstrip().lower()
    if (sen == "#"):
        break

    sen2 = ""
    for letter in sen:
        if ((97 <= ord(letter)) and (ord(letter) <= 122)):
            sen2 += letter
    senl = set(list(sen2))
    print(len(senl))
