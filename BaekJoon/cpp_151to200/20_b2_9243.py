# 9243

import sys

n = int(sys.stdin.readline())
first = sys.stdin.readline().rstrip()
second = sys.stdin.readline().rstrip()

nfir = ""
if (n % 2 == 1):
    for num in first:
        if (num == "0"):
            nfir += "1"
        else:
            nfir += "0"
else:
    nfir = first

if (nfir == second):
    print("Deletion succeeded")
else:
    print("Deletion failed")
