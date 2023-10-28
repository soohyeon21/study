# 10181

# join을 사용하기 위해서는 list의 값이 string이어야 한다.
# map을 이용해 int를 str로 바꿔주기

import sys

def findFactor(number):
    factors = []
    for n in range(1, number//2+1):
        if (number%n == 0):
            factors.append(n)
    return factors

while (1):
    num = int(sys.stdin.readline())
    if (num == -1):
        break

    factor = findFactor(num)
    
    if (sum(factor) == num):
        print(f"{num} = {' + '.join(map(str, factor))}")
    else:
        print(f'{num} is NOT perfect.')
