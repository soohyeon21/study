# 10372

# seg를 굳이 dictionary 말고 list로 사용해도 됐을듯.

# state="Impossible"로 설정하고, (cnt==n)일때 state를 해당 시간으로 바꿔도 됨.

import sys

n = int(sys.stdin.readline())

seg = {"0":6, "1":2, '2':5, '3':5, '4':4, '5':5, '6':6, '7':3, '8':7, '9':6}

state = False
for mm in range(23*60+59+1):
    display = str(mm//60).zfill(2) + str(mm%60).zfill(2)
    cnt = sum(seg[digit] for digit in display)
    if (cnt == n):
        print(display[:2]+":"+display[2:])
        state = True
        break

if (not state):
    print("Impossible")
