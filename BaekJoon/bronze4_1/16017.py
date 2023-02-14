# 16017

import sys

num = ""
for _ in range(4):
    num += sys.stdin.readline().rstrip()

if (((num[0] == "8") or (num[0] == "9")) and ((num[-1] == "8") or (num[-1] == "9")) and (num[1] == num[2])):
    print("ignore")
else:
    print("answer")
