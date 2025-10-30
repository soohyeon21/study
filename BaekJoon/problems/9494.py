# 9494

import sys

while (1):
    n = int(sys.stdin.readline())
    if (n == 0):
        break
    
    text = [sys.stdin.readline().replace('\n', '')+' ' for _ in range(n)]

    begin = 0
    end = 0
    for i in range(n):
        end = text[i][begin:].find(' ')
        if (end != -1):
            begin += end

    print(begin+1)
