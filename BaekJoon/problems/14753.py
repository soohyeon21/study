# 14753

# 경우만 잘 나누면 비교적 간단하게 구현 가능하다.

import sys

n = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))

plus = sorted([card for card in cards if card >= 0], reverse=True)
minus = sorted([card for card in cards if card < 0])

cand = []

# 1) 2개
## (+, +)
if (len(plus) > 1):
    cand.append(plus[0]*plus[1])
## (-, -)
if (len(minus) > 1):
    cand.append(minus[0]*minus[1])

# 2) 3개
## (+, +, +)
if (len(plus) > 2):
    cand.append(plus[0]*plus[1]*plus[2])
## (-, -, +)
if ((len(plus) > 0) and (len(minus) > 1)):
    cand.append(minus[0]*minus[1]*plus[0])

print(max(cand))
