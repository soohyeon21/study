# 11365

# while(True) + break 하는 거 말고는 다른 방법이 없나?

import sys

cipher = "" # not needy
while (True):
    cipher = sys.stdin.readline().rstrip()
    if (cipher == "END"):
        break
    print(cipher[::-1])
