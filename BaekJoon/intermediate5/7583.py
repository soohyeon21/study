# 7583

import sys

while (1):
    sent = sys.stdin.readline().split()
    if (sent[0] == "#"):
        break

    for word in sent:
        if (len(word) <= 3):
            print(word, end=" ")
        else:
            print(word[0]+word[1:-1][::-1]+word[-1], end=" ")
    print()
