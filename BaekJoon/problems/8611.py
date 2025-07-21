# 8611

import sys

n = int(sys.stdin.readline())

posi = {}
for base in range(2, 11):
    alter = ""
    portion = n
    while (portion != 0):
        alter = str(portion%base) + alter
        portion //= base

    if ((alter == alter[::-1]) and (alter != '')):
        posi[base] = alter

if (len(posi) == 0):
    print("NIE")
else:
    for key in posi.keys():
        print(key, posi[key])
