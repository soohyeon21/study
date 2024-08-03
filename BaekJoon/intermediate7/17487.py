# 17487

import sys

ipt = sys.stdin.readline().rstrip()
left = "qwertyasdfgzxcvb"
right = "uiophjklnm"

extra = 0
lcnt = 0
rcnt = 0
for letter in ipt:
    if (letter.isupper()):
        extra += 1
    if (letter.isspace()):
        extra += 1
        
    if (letter.lower() in left):
        lcnt += 1
    elif (letter.lower() in right):
        rcnt += 1

for i in range(extra):
    if (lcnt <= rcnt):
        lcnt += 1
    else:
        rcnt += 1

print(lcnt, rcnt)
