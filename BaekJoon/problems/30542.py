# 30542

import sys

text = sys.stdin.readline().rstrip()

after = ""
for letter in text.lower():
    if (letter.isalpha()):
        after += letter

isPal = False
for i in range(len(after)-1):
    for j in range(i+2, len(after)+1):
        if (after[i:j] == after[i:j][::-1]):
            isPal = True

if (after == after[::-1]):
    isPal = True

if (isPal):
    print("Palindrome")
else:
    print("Anti-palindrome")
