# 26264

# 하나만 count하고 n에서 빼도 된다.

import sys

n = int(sys.stdin.readline())
memo = sys.stdin.readline().rstrip()

bnum = memo.count("bigdata")
snum = memo.count("security")

if (bnum > snum):
    print("bigdata?")
elif (bnum < snum):
    print("security!")
elif (bnum == snum):
    print("bigdata? security!")
