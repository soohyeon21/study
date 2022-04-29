# 1159

import sys

n = int(sys.stdin.readline())
lname = []
possi = ""

for _ in range(n):
    last = sys.stdin.readline().rstrip()[0]
    lname.append(last)

for i in range(97, 123):
    if (lname.count(chr(i)) >= 5):
        possi += chr(i)

if (len(possi) == 0):
    print("PREDAJA")
else:
    print(possi)
