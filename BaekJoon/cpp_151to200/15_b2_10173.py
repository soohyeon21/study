# 10173

import sys

while (True):
    sent = sys.stdin.readline().rstrip()
    if (sent == "EOI"):
        break

    lsent = sent.lower()
    if ("nemo" in lsent):
        print("Found")
    else:
        print("Missing")
