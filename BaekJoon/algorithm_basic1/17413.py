# 17413

# isBracketOpen 대신 isTag도 이름으로 괜찮았을듯.

import sys

s = sys.stdin.readline().rstrip()

# 사실 필요 없는 부분
##bracket = []
##for i in range(len(s)):
##    if (s[i] in "<>"):
##        bracket.append(i)

word = ""
result = ""
isBracketOpen = False
for j in range(len(s)):
    if (s[j] == "<"):
        result += word[::-1]
        isBracketOpen = True
        word = "<"
    elif (s[j] == ">"):
        result += word+">"
        isBracketOpen = False
        word = ""
    elif ((s[j] == " ") and (not isBracketOpen)):
        result += word[::-1]+" "
        word = ""
    else:
        word += s[j]
        if (j == len(s)-1):
            result += word[::-1]

print(result)
