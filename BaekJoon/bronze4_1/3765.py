# 3765

# rstrip()을 쓰면 틀린다.
# "respecting the use of space exactly as in the input."

import sys

ipt = sys.stdin.readlines()
for one in ipt:
    print(one.replace('\n', ''))
