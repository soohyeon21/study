# 30224

import sys

num = int(sys.stdin.readline())

if (('7' not in str(num)) and (num%7 != 0)):
    print(0)
elif (('7' not in str(num)) and (num%7 == 0)):
    print(1)
elif (('7' in str(num)) and (num%7 != 0)):
    print(2)
elif (('7' in str(num)) and (num%7 == 0)):
    print(3)
