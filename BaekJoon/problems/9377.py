# 9377

import sys

while (1):
    n = int(sys.stdin.readline())
    if (n == 0):
        break

    words = []
    mlen = 100
    for _ in range(n):
        word = sys.stdin.readline().rstrip()
        words.append(word)
        mlen = min(len(word), mlen)

    cnt = 0
    for i in range(mlen-1):
        for w in range(n):
            words[w] = words[w][1:]
        if (len(set(words)) < n):
            break
        cnt += 1

    print(cnt)
