# 4821

import sys

while (1):
    pages = int(sys.stdin.readline())
    if (pages == 0):
        break
    
    rang = sys.stdin.readline().split(",")
    docx = {i:0 for i in range(1, pages+1)}
    
    for r in rang:
        se = list(map(int, r.split("-")))
        for j in range(se[0], se[-1]+1):
            try:
                docx[j] += 1
            except:
                pass

    print(pages - list(docx.values()).count(0))
