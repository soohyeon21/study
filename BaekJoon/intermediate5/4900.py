# 4900

import sys

digit_to_code = {0:'063'}

while (1):
    ipt = sys.stdin.readline().rstrip()
    if (ipt == "BYE"):
        break

    a, b = ipt.split('+')
    b = b[:-1]

    
