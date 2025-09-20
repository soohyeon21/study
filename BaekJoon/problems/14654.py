# 14654

# 더 간단하게 작성할 수 있는 방법?

import sys

def game(rcp):
    win0 = [(2, 1), (3, 2), (1, 3)]
    if (rcp in win0):
        return 0
    elif (rcp[::-1] in win0):
        return 1
    elif (rcp[0] == rcp[1]):
        return 2


n = int(sys.stdin.readline())

nam = list(map(int, sys.stdin.readline().split()))
new = list(map(int, sys.stdin.readline().split()))

swin = 0
single_nam = 0
single_new = 0
nam_new = True
new_new = True
for i in range(n):
    win = game((nam[i], new[i]))
    if (win == 0): # 남 win
        nam_new = False
        new_new = True
        single_nam += 1
        swin = max(swin, single_nam, single_new)
        single_new = 0
    elif (win == 1): # 뉴 win
        nam_new = True
        new_new = False
        single_new += 1
        swin = max(swin, single_nam, single_new)
        single_nam = 0
    elif (win == 2):
        if (nam_new): # 남 win
            nam_new = False
            new_new = True
            single_nam += 1
            swin = max(swin, single_nam, single_new)
            single_new = 0
        elif (new_new): # 뉴 win
            nam_new = True
            new_new = False
            single_new += 1
            swin = max(swin, single_nam, single_new)
            single_nam = 0

print(swin)
