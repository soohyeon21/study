# 4153

# 모든 원소를 돌아가며 check할 필요없이
# 가장 큰 수를 뽑고, 그 수가 빗변이 될 수 있는지 확인하면 간단해진다.

import sys

def tri_check(inlst):
    lst = inlst
    chck = []
    for _ in range(3):
        if (lst[0]**2 == lst[1]**2 + lst[2]**2):
            chck.append(True)
        else:
            chck.append(False)
        lst.append(lst[0])
        del lst[0]
    if (True in chck):
        return True
    else:
        return False

while (True):
    value = list(map(int, sys.stdin.readline().split()))
    if (value == [0, 0, 0]):
        break
    elif (tri_check(value)):
        print("right")
    else:
        print("wrong")
