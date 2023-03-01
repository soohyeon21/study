# 5300

import sys

pirate = int(sys.stdin.readline())
for i in range(1, pirate+1):
    print(i, end=" ")
    if ((i % 6 == 0) or (i == pirate)):
        print("Go!", end=" ")
