# 31663

import sys

n = int(sys.stdin.readline())

longest = 0
word = []
for _ in range(n):
    ipt = sys.stdin.readline().rstrip()
    longest = max(longest, len(ipt))
    word.append(ipt)

result = [0]*longest
cnt = [0]*longest
for w in word:
    for i in range(len(w)):
        result[i] += ord(w[i])
        cnt[i] += 1

for j in range(longest):
    print(chr(int(result[j]/cnt[j])), end='')
