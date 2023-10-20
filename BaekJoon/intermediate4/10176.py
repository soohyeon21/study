# 10176

# 새로 list를 만들어서 모든 알파벳의 짝이 존재하는지 확인하는 방법

# for letter in word에 대해서 짝이 존재하는지만 확인하는 풀이도 있다.

import sys

n = int(sys.stdin.readline())
for _ in range(n):
    word = sys.stdin.readline().rstrip().upper()
    nword = set()
    for letter in word:
        if (65 <= ord(letter) <= 90):
            nword.add(chr(155-ord(letter)))
        else:
            nword.add(letter)
    
    if (nword == set(word)):
        print("Yes")
    else:
        print("No")
