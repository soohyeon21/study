# 15087

import sys

msg = sys.stdin.readline().rstrip()

# Divide
half1 = msg[:len(msg)//2]
half2 = msg[len(msg)//2:]

# Rotate
val1 = sum(ord(letter)-65 for letter in half1)
val2 = sum(ord(letter)-65 for letter in half2)
new1, new2 = "", ""
for i in range(len(msg)//2):
    new1 += chr((ord(half1[i])-65+val1)%26+65)
for j in range(len(msg)//2):
    new2 += chr((ord(half2[j])-65+val2)%26+65)

# Merge
merged = ""
for k in range(len(msg)//2):
    merged += chr(((ord(new1[k])-65) + (ord(new2[k])-65))%26 + 65)

print(merged)
