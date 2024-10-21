# 13775

# k = k+1 if k<25 else 1 # 한 줄로 가능

import sys

k = int(sys.stdin.readline())
crypt = sys.stdin.readline().replace("\n", '')

rst = ""
for letter in crypt:
    if (letter.isalpha()):
        rst += chr((ord(letter)-97-k+26)%26+97)
        k = (k+1)%25
        if (k == 0):
            k = 25
    else:
        rst += letter

print(rst)
