# 1384

import sys

tcase = 1
while (1):
    n = int(sys.stdin.readline())
    if (n == 0):
        break

    names = []
    papers = []
    for _ in range(n):
        tmp = sys.stdin.readline().split()
        names.append(tmp[0])
        papers.append(tmp[1:])

    isNasty = False
    nastyPair = []
    for i in range(n): # 각 사람에 대해
        for j in range(n-1): # 각 메시지에 대해
            if (papers[i][j] == "N"):
                idx = (i+n - (j+1))%n
                isNasty = True
                nastyPair.append((names[idx], names[i]))

    print(f"Group {tcase}")
    if (isNasty):
        for pair in nastyPair:
            print(f"{pair[0]} was nasty about {pair[1]}")
    else:
        print("Nobody was nasty")
    print()

    tcase += 1
