# 4287

import sys

while (1):
    ipt = sys.stdin.readline().rstrip()
    if (ipt ==  "#"):
        break

    words = ipt.split()
    last = ""
    for idx in range(len(words[0])):
        dist = (ord(words[1][idx]) - ord(words[0][idx]) +26)%26
        last += chr((ord(words[2][idx])-97+dist)%26 + 97)
    print(*words, last)
