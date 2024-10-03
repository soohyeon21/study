# 9289

import sys

morse = {".-":"A", "-...":"B", "-.-.":"C", "-..":"D", ".":"E", "..-.":"F",
         "--.":"G", "....":"H", "..":"I", ".---":"J", "-.-":"K", ".-..":"L",
         "--":"M", "-.":"N", "---":"O", ".--.":"P", "--.-":"Q", ".-.":"R",
         "...":"S", "-":"T", "..-":"U", "...-":"V", ".--":"W", "-..-":"X",
         "-.--":"Y", "--..":"Z"}

t = int(sys.stdin.readline())
for idx in range(1, t+1):
    ipt = sys.stdin.readline().split()
    
    word = ""
    for one in ipt:
        word += morse[one]

    print(f"Case {idx}: {word}")
