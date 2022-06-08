# 6321

import sys

n = int(sys.stdin.readline())
for j in range(1, n+1):
    name = sys.stdin.readline().rstrip()
    new = ""
    for i in range(len(name)):
        if (ord(name[i]) == 90): # 그냥 "Z"일때로 해도 되는걸.
            new += "A"
        else:
            new += chr(ord(name[i]) + 1)
    print("String #%d" %(j))
    print(new + "\n")
