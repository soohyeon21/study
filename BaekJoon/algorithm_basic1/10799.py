# 10799

import sys

ipt = sys.stdin.readline().rstrip()
openb = 0
fragments = 0

for i in range(len(ipt)):
    if (ipt[i] == "("):
        openb += 1
    if (ipt[i] == ")"): # or 'else'
        if (ipt[i-1] == "("):
            openb -= 1
            if (openb):
                fragments += openb
        else:
            openb -= 1
            fragments += 1

print(fragments)
