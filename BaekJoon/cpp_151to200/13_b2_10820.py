# 10820

# 예제를 꼼꼼히 확인하자.

# .isupper() .islower() .isdigit() .isspace() # 문자열 함수 사용 가능!!

import sys

while (True):
    s = sys.stdin.readline().rstrip('\n')
    if (s == ""):
        break

    scnt = 0
    ccnt = 0
    ncnt = 0
    bcnt = 0

    for letter in s:
        asc = ord(letter)
        if (97 <= asc <= 122):
            scnt += 1
        elif (65 <= asc <= 90):
            ccnt += 1
        elif (48 <= asc <= 57):
            ncnt += 1
        elif (asc == 32):
            bcnt += 1
    print(scnt, ccnt, ncnt, bcnt)
