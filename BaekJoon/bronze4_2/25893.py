# 25893

# sort해서 0, 1, 2 index의 값이 10 이상인지 확인하는 방법도 있고
# print문을 list에 넣고 list[cnt] 하는 방법도 있다.

import sys

n = int(sys.stdin.readline())
for _ in range(n):
    nlist = list(map(int, sys.stdin.readline().split()))
    cnt = 0
    for num in nlist:
        if (num >= 10):
            cnt += 1

    print(*nlist)
    if (cnt == 3):
        print("triple-double")
    elif (cnt == 2):
        print("double-double")
    elif (cnt == 1):
        print("double")
    else:
        print("zilch")
    print()
