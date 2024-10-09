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
            subn = ord(fin)-65
            ul = [97, 65][int(letter.isupper())]
            after = ord(letter) - ul - subn
            after = (after + 26)%26 + ul
            rst += chr(after)
        else:
            rst += letter
            
    print(rst)
