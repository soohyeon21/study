# 9046

# .replace(" ", "")로 공백 없앨 수 있다.

import sys

t = int(sys.stdin.readline())
for _ in range(t):
    cipher = sys.stdin.readline().rstrip()
    cset = set(cipher)
    dcipher = {}
    for letter in cset:
        if (letter != " "):
            dcipher[letter] = cipher.count(letter)
    citems = sorted(list(dcipher.items()), key=lambda x:-x[1])
    if (len(citems) == 1):
        print(citems[0][0])
    elif (citems[0][1] == citems[1][1]):
        print("?")
    else:
        print(citems[0][0])
