# 10987

# list말고 문자열 "aeiou"에 letter가 있냐고 if문 작성해도 될듯.

import sys

vowel = ["a", "e", "i", "o", "u"]
word = sys.stdin.readline()

cnt = 0
for letter in word:
    if (letter in vowel):
        cnt += 1

print(cnt)
