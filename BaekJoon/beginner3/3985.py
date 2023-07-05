# 3985

# "각 경우에 조건을 만족하는 방청객이 두 명 이상이라면 그중 번호가 가장 작은 방청객의 번호를 출력한다."

import sys

l = int(sys.stdin.readline())
n = int(sys.stdin.readline())
pk = [tuple(map(int, sys.stdin.readline().split())) for x in range(n)]
##print(pk) #
cake = [0 for y in range(l)]

for person in range(n):
    for pki in range(pk[person][0]-1, pk[person][1]):
        if (cake[pki] == 0):
            cake[pki] = person+1
##        print(cake) #
expected = sorted([(i+1, pk[i][1]-pk[i][0]+1) for i in range(n)], key=lambda x:(x[1], -x[0]))
real = sorted([(i+1, cake.count(i+1)) for i in range(n)], key=lambda x:(x[1], -x[0]))

##print(expected) #
##print(real) #
print(expected[-1][0])
print(real[-1][0])
