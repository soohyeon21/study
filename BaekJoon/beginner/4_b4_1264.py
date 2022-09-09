# 1264

# sys.stdin.readline().rstrip() 다음에 lower()을 붙여도 된다.

import sys

vowel = "aeiou"
while (1):
    sen = sys.stdin.readline().rstrip().lower()
    if (sen == "#"):
        break

    cnt = 0
    for letter in sen:
        if (letter in vowel):
            cnt += 1
    print(cnt)
