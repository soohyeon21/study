# 15117

import sys

n = int(sys.stdin.readline())
ls = [sys.stdin.readline().rstrip() for _ in range(n)]

order = ''
for i in range(n):
    if (i < 10):
        order += str(i)
    else:
        order += chr(i+55)

## is Latin Square?
ls_state = True
for j in range(n):
    if (set(ls[j]) != set(order)):
        ls_state = False
        break
    
    col = ''
    for k in range(n):
        col += ls[k][j]
    if (set(col) != set(order)):
        ls_state = False

## is Reduced?
state = True
if (ls[0] != order): # row1
    state = False
if (''.join(line[0] for line in ls) != order): # leftmost col
    state = False


if (not ls_state):
    print("No")
elif (state):
    print("Reduced")
else:
    print("Not Reduced")
