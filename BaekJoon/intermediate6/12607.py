# 12607

import sys

text = {"0":" ", 'a':2, 'b':22, 'c':222, 'd':3, 'e':33, 'f':333,
        'g':4, 'h':44, 'i':444, 'j':5, 'k':55, 'l':555,
        'm':6, 'n':66, 'o':666, 'p':7, 'q':77, 'r':777, 's':777,
        't':8, 'u':88, 'v':888, 'w':9, 'x':99, 'y':999, 'z':9999}

n = int(sys.stdin.readline())
for idx in range(1, n+1):
    msg = sys.stdin.readline().rstrip()
    rst = str(text[msg[0]])
    for i in range(1, len(msg)):
        if (rst[-1] == str(text[msg[i]])[0]):
            rst += " "
        else:
            rst += str(text[msg[i]])
