# 11149

import sys

t = int(sys.stdin.readline())
for _ in range(t):
    msg = sys.stdin.readline().split()
    result = ""
    for word in msg:
        val = 0
        for letter in word:
            if (letter.isalpha()):
                val += ord(letter)-97
            elif (letter == " "):
                val += 26
        char = val%27
        result += chr(char+97) if char!=26 else " "
    print(result)
