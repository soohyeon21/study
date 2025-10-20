# 15071

# ex) msg-key-cip은 ord 상에서 아래와 같은 상관관계가 있다.
# (msg) SENDMOREMONKEYS : [18, 4, 13, 3, 12, 14, 17, 4, 12, 14, 13, 10, 4, 24, 18]
# (key) ACMSENDMOREMONK : [0, 2, 12, 18, 4, 13, 3, 12, 14, 17, 4, 12, 14, 13, 10]
# (cip) SGZVQBUQAFRWSLC : [18, 6, 25, 21, 16, 1, 20, 16, 0, 5, 17, 22, 18, 11, 2]

import sys

cipher = sys.stdin.readline().rstrip()
word = sys.stdin.readline().rstrip()

msg_ord = []
word_ord = [ord(letter)-65 for letter in word]

for i in range(len(cipher)):
    tmp = ((ord(cipher[i])-65) - word_ord[i]) % 26
    msg_ord.append(tmp)
    if (len(word_ord) < len(cipher)):
        word_ord.append(tmp)

for each in msg_ord:
    print(chr(each+65), end='')
