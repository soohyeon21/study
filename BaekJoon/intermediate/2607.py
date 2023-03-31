# 2607

# 어렵게 풀려면 어렵게 풀 수도 있는 문제ㅎ

# list(sys.stdin.readline().rstrip()) # ['a', 'b', 'c', 'd']

# a가 b에 영향을 안끼치려면
# a = b.copy()
# a = b[:]

import sys

n = int(sys.stdin.readline())
word = list(letter for letter in sys.stdin.readline().rstrip())

cnt = 0
for _ in range(n-1):
    subject = list(letter for letter in sys.stdin.readline().rstrip())
    compare = word.copy()

    notin = 0
    for letter in subject:
        if (letter in compare):
            compare.remove(letter)
        else:
            notin += 1

    if ((notin < 2) and (len(compare) < 2)):
        cnt += 1

print(cnt)
