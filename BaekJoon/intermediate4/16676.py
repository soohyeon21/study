# 16676

#
# sol1)
#
import sys

n = int(sys.stdin.readline())
sticker = 1

if (n <= 10):
    print(1)
else:
    while (n >= sticker):
        sticker = int(str(sticker) + "1")
    print(len(str(sticker//10)))



#
# sol2)
#
##import sys
##
##n = int(sys.stdin.readline())
##
##lenn = len(str(n))
##alldig = str(n)[0]*lenn
##sticker = lenn
##
##for i in range(lenn):
##    if (n <= (int(alldig)//10**i)*10**i):
##        sticker = lenn-i
##    else:
##        break
##
##sticker = max(sticker, str(n).count("0"))
##
##print(sticker)
