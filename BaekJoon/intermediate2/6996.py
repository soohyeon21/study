# 6996

# 다른 방법) a, b를 sort해서 똑같으면 애너그램이다.

import sys

t = int(sys.stdin.readline())

for _ in range(t):
    stra, strb = sys.stdin.readline().split()
    a = list(stra)
    b = list(strb)
    cnt = 0
    for i in range(len(stra)):
        if (stra[i] in b):
            b.remove(stra[i])
            cnt += 1
    if ((cnt == len(stra)) and (b == [])):
        state = ""
    else:
        state = "NOT "
    print(f"{stra} & {strb} are {state}anagrams.")
