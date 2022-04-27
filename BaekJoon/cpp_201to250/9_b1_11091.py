# 11091

# list.remove(값) # remove는 삭제하려는 값이 없으면 error가 발생한다.

import sys

n = int(sys.stdin.readline())
nalpha = """ .,?!'"0123456789"""

for _ in range(n):
    sen = list(sys.stdin.readline().rstrip().lower())
    sset = set(sen)
    #print(sen, sset)
    for letter in nalpha:
        if (letter in sset):
            sset.remove(letter)

    if (len(sset) == 26):
        print("pangram")
    else:
        mis = ""
        for i in range(97, 123):
            if chr(i) not in sset:
                mis += chr(i)
        print("missing", mis)
