# 15829

# python mod 연산 기호 %

import sys

r = 31
m = 1234567891

l = int(sys.stdin.readline())
word = sys.stdin.readline().rstrip()

hashn = 0
for i in range(l):
    letter_ord = ord(word[i])-96
    hashn += (letter_ord) * r**i

print(hashn % m)
