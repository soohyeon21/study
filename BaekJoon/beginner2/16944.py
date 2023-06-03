# 16944

import sys

n = int(sys.stdin.readline())
pw = sys.stdin.readline().rstrip()

num = False
low = False
upp = False
spe = False
special = "!@#$%^&*()-+"

for letter in pw:
    if (letter.isdigit()):
        num = True
    if (letter.islower()):
        low = True
    if (letter.isupper()):
        upp = True
    if (letter in special):
        spe = True

more = 0
if (not num):
    more += 1
if (not low):
    more += 1
if (not upp):
    more += 1
if (not spe):
    more += 1
if (n+more < 6):
    more = 6 - n

print(more)
