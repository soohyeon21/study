# 2954

# 헤헷
# (vow in vowel) 상화이면 굳이 뒤의 조건은 없어도 될듯?

import sys

enc = sys.stdin.readline().rstrip()
vowel = ['a', 'e', 'i', 'o', 'u']

i = 0
dec = ""
while (i < len(enc)):
    vow = enc[i]
    if ((vow in vowel) and (enc[i:i+3] == (vow+'p'+vow))):
        dec += vow
        i += 3
    else:
        dec += enc[i]
        i += 1
print(dec)
