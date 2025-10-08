# 2824

# 두 약수 간의 gcf를 찾고, 전체에 곱해주고, 다시 각 약수를 나눠준다.

# 모든 수를 싹 다 곱해서, 두 큰 수의 gcf를 찾아도 되긴 함.

import sys

def gcf(a, b):
    while (b != 0):
        num = a%b
        a = b
        b = num
    return a

n = int(sys.stdin.readline())
nnum = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
mnum = list(map(int, sys.stdin.readline().split()))

factor = 1
for i in range(n):
    for j in range(m):
        small_gcf = gcf(nnum[i], mnum[j])
        factor *= small_gcf
        nnum[i] //= small_gcf
        mnum[j] //= small_gcf

print(str(factor)[-9:])
