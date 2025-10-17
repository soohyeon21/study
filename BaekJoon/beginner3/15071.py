# 15071

import sys

cipher = sys.stdin.readline().rstrip()
word = sys.stdin.readline().rstrip()

msg_ord = []
for i in range(len(word)):
    msg_ord.append(((ord(cipher[i])-65) - (ord(word[i])-65)) % 26)

word_ord = [ord(letter)-65 for letter in word]+msg_ord[len(word):2*len(word)]

for k in range(len(cipher)//len(word)-1):
    print(f"k={k}")
    word_ord += msg_ord[(k)*len(word):(k+1)*len(word)]
    for i in range((k+1)*len(word), (k+2)*len(word)):
        msg_ord.append(((ord(cipher[i])-65) - word_ord[i]) % 26)
        print(f"msg_ord : {msg_ord}")
        print(f"original: {[18, 4, 13, 3, 12, 14, 17, 4, 12, 14, 13, 10, 4, 24, 18]}")
        print(f"key_ord : {word_ord}")
        print(f"original: {[0, 2, 12, 18, 4, 13, 3, 12, 14, 17, 4, 12, 14, 13, 10]}")
        print(f"cip_ord : {[18, 6, 25, 21, 16, 1, 20, 16, 0, 5, 17, 22, 18, 11, 2]}")
        print("---------")

print(msg_ord)
