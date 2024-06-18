# 9440

# n에도 '0'이 포함될 수 있다.
# 첫째 자리 수는 0이 아닌 수 -> 0 먼저 소진 -> 남은 수 순서대로 배정
# 같은 자리 수이면 num1이 더 작고, 자리수 다르면 num1의 첫번째 숫자가 개중 가장 작은 수

import sys

while (1):
    tmp = sys.stdin.readline().rstrip()
    if (tmp == "0"):
        break

    tmp = tmp.split()
    n = int(tmp[0])
    tmp = tmp[1:]

    ipt = []
    zeros = 0
    for one in tmp:
        if (one == "0"):
            zeros += 1
        else:
            ipt.append(one)
    half_z = zeros//2
    ipt.sort()

    num1 = ipt[0] + "0"*(zeros-half_z)
    num2 = ipt[1] + "0"*half_z
    odd = 0
    if (half_z*2 != zeros):
        odd = 1
    for i in range(len(ipt)-2):
        if (i%2 == odd):
            num1 += ipt[i+2]
        elif (i%2 != odd):
            num2 += ipt[i+2]

    print(int(num1) + int(num2))
