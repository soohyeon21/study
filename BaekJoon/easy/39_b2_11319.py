# 11319

# list말고 "AEIOUaeiou" 문자열에 있는지 유무 확인하는 방법도 있는걸

import sys

vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']

s = int(sys.stdin.readline())
for _ in range(s):
    vow = 0
    con = 0
    sentence = sys.stdin.readline().rstrip()
    for letter in sentence:
        if (letter in vowels):
            vow += 1
        elif (letter == ' '):
            continue
        else:
            con += 1
    print(con, vow)
