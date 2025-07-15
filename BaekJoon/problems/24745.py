# 24745

# "If there are no letters or digits in the input string, the output should be NO."

import sys

morse = {'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.',
         'G':'--.', 'H':'....', 'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..',
         'M':'--', 'N':'-.', 'O':'---', 'P':'.--.', 'Q':'--.-', 'R':'.-.',
         'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-',
         'Y':'-.--', 'Z':'--..', '0':'-----', '1':'.----', '2':'..---',
         '3':'...--', '4':'....-', '5':'.....', '6':'-....', '7':'--...',
         '8':'---..', '9':'----.'}

s = sys.stdin.readline().rstrip()

morse_s = ""
islein = False
for letter in s.upper():
    if ((65 <= ord(letter) <= 90) or (48 <= ord(letter) <= 57)):
        morse_s += morse[letter]
        islein = True

if (not islein):
    print('NO')
elif (morse_s == morse_s[::-1]):
    print("YES")
else:
    print('NO')
