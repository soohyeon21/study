# 32357

# word의 절반의 [::-1] 말고, word 전체의 [::-1]를 비교해도 되었다.

import sys

n = int(sys.stdin.readline())
words = [sys.stdin.readline().rstrip() for _ in range(n)]

pal = 0
for word in words:
    if (word[:len(word)//2] == word[len(word)//2:][::-1]):
        pal += 1

print(pal*(pal-1))
