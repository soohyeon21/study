# 1919

import sys

word1 = list(sys.stdin.readline().rstrip())
word2 = list(sys.stdin.readline().rstrip())
cnt = 0

for letter in word1:
    if (letter in word2):
        word2.remove(letter)
        cnt += 1

print(len(word1+word2)-cnt)
