# 5637

# 다들 're' module의 정규표현식 r'[a-zA-Z-]+'를 사용하더라.

# 궁금한 점: 입력의 마지막을 의미하는 'E-N-D'도 단어로 인정해주는거 아닌가? 

import sys

ok = [i for i in range(65, 91)] + [j for j in range(97, 123)] + [45]
not_ok = []

docu = sys.stdin.read()

for letter in docu:
    if (ord(letter) not in ok):
        not_ok.append(ord(letter))

for num in not_ok:
    docu = " ".join(docu.split(chr(num)))
docu = docu.split()

length_l = [len(word) for word in docu]

print(docu[length_l.index(max(length_l))].lower())
