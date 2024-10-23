# 11297

import sys

while (1):
    m, d, y = map(int, sys.stdin.readline().split())
    if (m == 0):
        break
    
    encrypt = sys.stdin.readline().replace("\n", "")
    
    shift = (m+d+y)%25 + 1

    rst = ""
    for letter in encrypt:
        if (letter.isalpha()):
            rst += chr(((ord(letter)-97) - shift + 26)%26 + 97)
        else:
            rst += letter

    print(rst)
