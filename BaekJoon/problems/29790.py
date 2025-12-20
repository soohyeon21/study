# 29790

import sys

n, u, l = map(int, sys.stdin.readline().split())

baek = False
maple = False
if (n >= 1000):
    baek = True
if ((u >= 8000) or (l >= 260)):
    maple = True

if (baek and maple):
    print("Very Good")
elif (baek):
    print("Good")
else:
    print("Bad")
