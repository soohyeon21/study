# 5222

import sys

t = int(sys.stdin.readline())
for _ in range(t):
    word, plain = sys.stdin.readline().split()
    repeat = (word*(len(plain)//len(word)+1))[:len(plain)]

    rst = ""
    for i in range(len(plain)):
        rst += chr(((ord(plain[i])-65)+(ord(repeat[i])-65))%26+65)

    print(f"Ciphertext: {rst}")
