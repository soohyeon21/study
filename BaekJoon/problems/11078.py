# 11078

import sys

pin = sys.stdin.readline().rstrip()
pattern = sys.stdin.readline().rstrip()

result = ''
idx = 0
for digit in pattern:
    if (digit.islower()):
        result += pin[idx:idx+ord(digit)-96]
        idx += ord(digit)-96
    else:
        idx += ord(digit)-64

if (idx == len(pin)):
    output = sum(map(int, list(result)))
    print(output)
else:
    print('non sequitur')
