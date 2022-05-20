# 10769

import sys

sad = ":-("
happy = ":-)"

text = sys.stdin.readline().rstrip()
scnt = text.count(sad)
hcnt = text.count(happy)

if ((scnt == 0) and (hcnt == 0)):
    print("none")
elif (scnt == hcnt):
    print("unsure")
elif (scnt > hcnt):
    print("sad")
elif (scnt < hcnt):
    print("happy")
