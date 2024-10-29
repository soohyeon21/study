# 14040

# or word[i:j]

# max(len)이 40이기 때문에 단순 반복 가능.

import sys

word = sys.stdin.readline().rstrip()

longest = 1
for i in range(len(word)):
    nword = word[i:]
    for j in range(1, len(nword)+1):
        nnword = nword[:j]
        if (nnword == nnword[::-1]):
            longest = max(longest, len(nnword))

print(longest)
