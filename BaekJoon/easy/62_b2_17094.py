# 17094

import sys

s = int(sys.stdin.readline())
string = sys.stdin.readline().rstrip()

cnte = string.count("e")
cnt2 = string.count("2")

if (cnte > cnt2):
    print("e")
elif (cnte < cnt2):
    print(2)
else:
    print("yee")
