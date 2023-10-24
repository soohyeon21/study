# 16462

# "some_string".replace("0", "9").replace("6", "9") # replace 연달아서 가능

# floor&ceil 말고 int(), int()+1 도 가능

import sys
import math

n = int(sys.stdin.readline())
test = 0
for _ in range(n):
    newn = ""
    num = sys.stdin.readline().rstrip()
    for digit in num:
        if (digit in "06"):
            newn += "9"
        else:
            newn += digit
    test += min(100, int(newn))
avg = test/n

if (avg%1 < 0.5):
    print(math.floor(avg))
else:
    print(math.ceil(avg))
