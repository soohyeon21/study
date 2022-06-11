# 10384

# cnt에서 min값을 뽑아다가 pangram1~3 판단하는 방법도 있다.

import sys

n = int(sys.stdin.readline())

for k in range(1, n+1):
    sen = sys.stdin.readline().rstrip()
    sen = sen.lower()
    nsen = ""
    state = ""
    cnt = []
    for letter in sen:
        if ((97 <= ord(letter)) and (ord(letter) <= 122)):
            nsen += letter
    if (len(set(nsen)) < 26):
        state = "Not a pangram"
    else: # 여기서부터는 무조건 pangram이기는 함.
        for i in range(97, 123):
            cnt.append(nsen.count(chr(i)))

        state = "Pangram!"
        if (1 not in cnt):
            state = "Double pangram!!"
        if (2 not in cnt):
            state = "Triple pangram!!!"
        
    print(f"Case {k}: {state}")
