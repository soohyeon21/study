# 4084

# '만약 네 정수가 2^n보다 작다면, 3*n번 이내에 수렴한다'는 조건은 사용하지 않았다.

import sys
##import math

while (1):
    cnt = 0
    num = list(map(int, sys.stdin.readline().split()))
    if (num == [0, 0, 0, 0]):
        break
    elif (num == [num[0]]*4):
        print(cnt)
        continue
    
##    many = math.ceil(math.log(2, max(num)))
##    for _ in range(many):
    while (1):
        num = [abs(num[0]-num[1]), abs(num[1]-num[2]), abs(num[2]-num[3]), abs(num[3]-num[0])]
        cnt += 1
        if (num == [num[0]]*4):
            print(cnt)
            break
