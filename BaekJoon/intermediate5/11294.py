# 11294

# divmod(x, y) # Return the tuple (x//y, x%y)

import sys

def change(base, num):
    result = ""
    while (num != 0):
        digit = num%base
        if (digit >= 10):
            result += chr(digit+55)
        else:
            result += str(digit)
        num //= base
    return result[::-1]

while (1):
    creature = sys.stdin.readline().rstrip()
    if (creature == "#"):
        break
    
    system = int(sys.stdin.readline())
    dnum = int(sys.stdin.readline())
    after = change(system, dnum)
    print(creature, dnum, after, sep=", ")
