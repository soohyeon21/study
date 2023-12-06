# 11292

import sys

while (1):
    n = int(sys.stdin.readline())
    if (n == 0):
        break

    tcase = []
    for i in range(1, n+1):
        name, m = sys.stdin.readline().split()
        tcase.append([name, float(m), i])
        
    tcase.sort(key=lambda x:(-x[1], x[2]))
    tallest = tcase[0][1]
    for person in tcase:
        if (person[1] == tallest):
            print(person[0], end=" ")
        else:
            print()
            break
