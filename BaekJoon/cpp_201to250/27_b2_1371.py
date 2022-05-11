# 1371

# sys.stdin.read()를 쓰면 내가 결과를 확인 못하는 걸?
# 왜 while-try-except EOFError-break는 못 쓰는 걸까

# 일일이 안세고 count() 써도 된다.
# if로 " ", "\n" 안거르고 replace로 아예 전처리 해주는 방법도 있다.

import sys

sen = sys.stdin.read()

alp = [0 for x in range(26)]

for letter in sen:
    if ((letter != " ") and (letter != "\n")):
        alp[ord(letter) - 97] += 1

for i in range(len(alp)):
    if (alp[i] == max(alp)):
        print(chr(i+97), end="")


