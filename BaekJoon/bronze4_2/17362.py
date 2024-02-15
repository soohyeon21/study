# 17362

import sys

hand = {0:2, 1:1, 2:2, 3:3, 4:4, 5:5, 6:4, 7:3}

n = int(sys.stdin.readline())
print(hand[n%8])
