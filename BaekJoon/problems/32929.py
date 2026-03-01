# 32929

import sys

x = int(sys.stdin.readline())

character = 'UOS'[(x-1+3)%3]

print(character)
