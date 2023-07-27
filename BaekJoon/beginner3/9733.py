# 9733

import sys

bee = {"Re":0, "Pt":0, "Cc":0, "Ea":0, "Tb":0, "Cm":0, "Ex":0}
kind = ["Re", "Pt", "Cc", "Ea", "Tb", "Cm", "Ex"]
cnt = 0
while (1):
    ipt = sys.stdin.readline().split()
    cnt += len(ipt)
    if (len(ipt) == 0):
        break

    for work in ipt:
        if (work in kind):
            bee[work] += 1

for i in range(len(kind)):
    print(f"{kind[i]} {bee[kind[i]]} {bee[kind[i]]/cnt:.2f}")
print(f"Total {cnt} 1.00")
