# 10709

# 왼쪽부터 칸마다 확인하며 +1 하는 방법도 있다. boolean으로 cloud 유무 확인하면서.

import sys

h, w = map(int, sys.stdin.readline().split())
cloud = [sys.stdin.readline().rstrip() for x in range(h)]
time = []

for i in range(h):
    if ("c" in cloud[i]):
        back = list(cloud[i][::-1])
        tmptime = [-1 for x in range(w)]
        cindex = back.index("c")
        for j in range(w):
            if (j == cindex):
                tmptime[w-1-j] = 0
                back[cindex] = "."
                if ("c" in back):
                    cindex = back.index("c")
                else:
                    cindex = -1
            elif ((back[j] == ".") and (j < cindex)):
                tmptime[w-1-j] = cindex-j
    else:
        tmptime = [-1 for x in range(w)]
    time.append(tmptime)
    print(*time[i])
