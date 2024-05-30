# 7587

import sys

while (1):
    n = int(sys.stdin.readline())
    if (n == 0):
        break

    anagram = {}
    words = []
    for i in range(n):
        word = sys.stdin.readline().rstrip()
        word_set = sorted(list(word))
        anagram[word] = [word_set, 0, i]
        words.append(word)

    for j in range(n):
        for one in words[:j]+words[j+1:]:
            if (sorted(list(words[j])) == anagram[one][0]):
                anagram[one][1] += 1

    result = sorted(list(anagram.items()), key=lambda x:(-x[1][1], x[1][2]))
    print(result[0][0], result[0][1][1])
