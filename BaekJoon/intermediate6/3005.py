# 3005

# min("aab", "aba") # "aab" # 이렇게도 사전순 찾을 수 있다.

import sys

def find_words(word_line):
    result = []
    candidates = word_line.split("#")
    for cand in candidates:
        if (len(cand) > 1):
            result.append(cand)
    return result

r, c = map(int, sys.stdin.readline().split())
crossw = [sys.stdin.readline().rstrip() for _ in range(r)]

words = []
for row_line in crossw:
    words += find_words(row_line)

for i in range(c):
    col_line = ""
    for j in range(r):
        col_line += crossw[j][i]
    words += find_words(col_line)

words.sort()
print(words[0])
