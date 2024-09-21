# 6040

import sys

hexn = sys.stdin.readline().rstrip()
decin = int(hexn, 16)
octn = oct(decin)
print(octn[2:])
