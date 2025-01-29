#26742

import sys

socks = sys.stdin.readline().rstrip()

bpair = socks.count("B")//2
cpair = socks.count("C")//2


print(bpair+cpair)
