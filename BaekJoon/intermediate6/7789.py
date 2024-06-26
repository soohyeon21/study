# 7789

# 에라토스테네스의 체

# 첫번째 for문만 돌려서 풀면 시간 단축됨. 어차피 num1은 여섯 자리 수이다.

import sys

num1, pre = sys.stdin.readline().split()
num2 = int(pre+num1)
num1 = int(num1)

check = [True for _ in range(num2+1)]
for i in range(2, int(num2**0.5)+1):
    if (check[i] == 1):
        for j in range(2*i, num2+1, i):
            check[j] = False

if (check[num1] and check[num2]):
    print("Yes")
else:
    print("No")
