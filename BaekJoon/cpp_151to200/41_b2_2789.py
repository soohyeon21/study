# 2789

# word.replace(a, b) # word에서 a를 b로 바꾸기

import sys

word = sys.stdin.readline().rstrip()
cambridge = list('CAMBRIDGE')

enc = ""
for letter in word:
    if (letter not in cambridge):
        enc += letter

print(enc)
