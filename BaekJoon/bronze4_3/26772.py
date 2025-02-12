# 26772

import sys

n = int(sys.stdin.readline())

heart = [' @@@   @@@  ', '@   @ @   @ ', '@    @    @ ', '@         @ ', ' @       @  ', '  @     @   ', '   @   @    ', '    @ @     ', '     @      ']
for one in heart:
    print(one*n)
