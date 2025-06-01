# 29863

import sys

sleep = int(sys.stdin.readline())
wake = int(sys.stdin.readline())

print((wake-sleep+24)%24)
