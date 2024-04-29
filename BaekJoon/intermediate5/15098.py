# 15098

import sys

words = sys.stdin.readline().split()
if (len(set(words)) == len(words)):
    print("yes")
else:
    print("no")
