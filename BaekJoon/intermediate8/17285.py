# 17285

# XOR # 같으면 0 다르면 1

# 3^10 = 9, 9^10 = 3

import sys

s = sys.stdin.readline().replace("\n", '')

kval = ord(s[0]) ^ ord('C')

rst = ""
for letter in s:
    rst += chr(ord(letter) ^ kval)

print(rst)
