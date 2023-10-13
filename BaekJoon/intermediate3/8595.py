# 8595

#
# sol1) 시간초과
#
##import sys
##
##n = int(sys.stdin.readline())
##hidden = sys.stdin.readline().rstrip()
##num = ""
##for letter in hidden:
##    if (letter.isdigit()):
##        num += letter
##    else:
##        num += " "
##total = sum(int(strnum) for strnum in num.split())
##print(total)


import sys

n = int(sys.stdin.readline())
hidden = sys.stdin.readline().rstrip()
abc = [chr(A) for A in range(65, 91)] + [chr(a) for a in range(97, 123)]

for letter in abc:
    hidden = hidden.replace(letter, " ")

total = sum(int(strnum) for strnum in hidden.split())
print(total)
