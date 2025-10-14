# 34509

# 조건을 만족하는 수는 42 밖에 없다.

import sys

def findN():
    for num in range(10, 100):
        if (int(str(num)[::-1])%4 == 0):
            if (sum(map(int, list(str(num))))%6 == 0):
                if ('8' not in list(str(num))):
                    return num


print(findN())
