# 17285

# XOR # 같으면 0 다르면 1

# 3^10 = 9, 9^10 = 3, 3^9 = 10, 9^3 = 10

import sys

t = sys.stdin.readline().rstrip()
key_val = ord(t[0]) ^ ord("C")

rst = ""
for letter in t:
    rst += chr(ord(letter)^key_val)

print(rst)
