# 10347

import sys

ao = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."

while (1):
    ipt = sys.stdin.readline().split()
    if (ipt[0] == "0"):
        break

    num = int(ipt[0])
    word = ipt[1][::-1]
    result = ""
    for i in range(len(word)):
        result += ao[(ao.index(word[i])+num)%28]
    print(result)
