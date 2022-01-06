# 1550

# 2진수 bin() '0b..'
# 8진수 oct() '0o..'
# 16진수 hex() '0x..'

# int(숫자, 몇 진수) # int('0b10', 2)

import sys

hexa = sys.stdin.readline().rstrip()

print(int(hexa, 16))
