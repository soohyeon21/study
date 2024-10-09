# 9954

import sys

while (1):
    line = sys.stdin.readline().rstrip()
    if (line == "#"):
        break

    fin = line[-1]
    line = line[:-1]

    rst = ""
    for letter in line:
        if (letter.isalpha()):
            rst += chr(65+((ord(letter)-(ord(fin)-65)+26)%26))
        else:
            rst += letter
    print(rst)
