# 15947

import sys

n = int(sys.stdin.readline())
n -= 1

verse = n//14
th = n%14
song = 'baby sukhwan tururu turu very cute tururu turu in bed tururu turu baby sukhwan'.split()

if (th in [0, 1, 4, 5, 8, 9, 12, 13]):
    print(song[th])
else:
    ru_len = song[th].count('ru')+verse
    if (ru_len >= 5):
        print(f"tu+ru*{ru_len}")
    else:
        print(song[th] + 'ru'*verse)
