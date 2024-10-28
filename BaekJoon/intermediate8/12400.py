# 12400

import sys

adict = {'a': 'y', 'b': 'h', 'c': 'e', 'd': 's', 'e': 'o', 'f': 'c',
         'g': 'v', 'h': 'x', 'i': 'd', 'j': 'u', 'k': 'i', 'l': 'g',
         'm': 'l', 'n': 'b', 'o': 'k', 'p': 'r', 'q': 'z', 'r': 't',
         's': 'n', 't': 'w', 'u': 'j', 'v': 'p', 'w': 'f', 'x': 'm',
         'y': 'a', 'z': 'q'}

t = int(sys.stdin.readline())
for idx in range(1, t+1):
    ipt = sys.stdin.readline().rstrip()

    rst = ""
    for letter in ipt:
        if (letter.isalpha()):
            rst += adict[letter]
        else:
            rst += letter

    print(f"Case #{idx}: {rst}")
