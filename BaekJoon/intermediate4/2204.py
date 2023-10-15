# 2204

# "대소문자의 구분을 없앴을 때 똑같은 단어는 주어지지 않는다" 하였으므로 그냥 대/소문자 하나로 통일해서 sort하면 된다.

# .sort(key=str.upper) # 신기하구려

import sys

while (1):
    n = int(sys.stdin.readline())
    if (n == 0):
        break

    dobi = [sys.stdin.readline().rstrip() for _ in range(n)]
    #dobi.sort(key=lambda x:(x.lower())) # 가능
    #dobi.sort(key=str.upper) # 가능
    dobi.sort(key=lambda x:x.upper()) # 가능

    print(dobi[0])
