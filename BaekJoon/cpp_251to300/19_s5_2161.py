# 2161

# 어디서 IndexError가 난 거지??
# 그리고 또 왜 except-pass 처리를 해도 문제 없는거지??

import sys

n = int(sys.stdin.readline())
card = [x for x in range(1, n+1)]

try:
    while (1):
        print(card.pop(0), end=" ")
        if (len(card) == 1):
            print(card.pop())
            break
        card.append(card.pop(0))
except:
    pass
