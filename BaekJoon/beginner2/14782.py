# 14782

# 두번째 if문은 반드시 첫번째 if문에 종속되어야 한다.
# 그냥 range(1, n+1)로 찾아도 충분함ㅎ

import sys

n = int(sys.stdin.readline())

num = []
for i in range(1, int(n**(1/2))+2):
    if ((n % i == 0) and (i not in num)):
        num.append(i)
        if (n//i not in num):
            num.append(n//i)

print(sum(num))
