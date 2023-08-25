# 17294

import sys

k = sys.stdin.readline().rstrip()

d = 0
state = True
for i in range(len(k)-1):
    if (i == 0):
        d = int(k[1]) - int(k[0])
    if (int(k[i+1]) - int(k[i]) != d):
        state = False
        break

if (state):
    print("◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!")
else:
    print("흥칫뿡!! <(￣ ﹌ ￣)>")
