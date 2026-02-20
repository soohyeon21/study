# 9850

# 입력의 마지막에는 공백, 줄바꿈이 없는게 확실한가 보다.

# 'LIVE', 'CHIPMUNKS'를 직접 26개 variation을 만들고, 그게 cipher에 있는지 확인하는 방법도 있다.

import sys

cipher = sys.stdin.readline().rstrip()
tmp = cipher
for i in range(len(tmp)):
    if (not tmp[i].isalpha()):
        tmp = tmp.replace(tmp[i], ' ')

word4 = []
word9 = []
for word in tmp.split():
    if (len(word) == 4):
        word4.append(word)
    if (len(word) == 9):
        word9.append(word)

keyp = 0
for w4 in word4:
    for w9 in word9:
        if ((len(set(w4)|set(w9)) == 12) and (w4[1] == w9[2])):
            keyp = (ord(w9[0])-65) - 2

plane = ''
for letter in cipher:
    if (letter.isalpha()):
        plane += chr((ord(letter)-65 - keyp)%26 + 65)
    else:
        plane += letter

print(plane)
