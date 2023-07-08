# 6750

import sys

word = sys.stdin.readline().rstrip()
state = True
okletter = "IOSHZXN"

for letter in word:
    if (letter not in okletter):
        state = False

print("YES" if state else "NO")
