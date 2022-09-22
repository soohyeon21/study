# 6376

# n = 8일때가 문제였다. 소수점 아래 8번째 숫자까지만 존재하기 때문이다.
# 따라서 round() 말고 f-string으로 .9f를 해줘야 한다.
# (아니 그럼 n=0,1,2도 남는 자리수는 0으로 채우게 해야할거 아냐 궁시렁꿍시렁)

# 그냥 답을 복붙해도 맞는단다ㅎ

import sys
from math import factorial

print("n e")
print("-", "-"*11)

approx = 0
for i in range(10):
    approx += 1/factorial(i)
    if (i == 0 or i == 1):
        print(i, int(approx))
    elif (i == 2):
        print(i, approx)
    else:
        print(f'{i} {approx:.9f}')

#
# 꼼수. ㅋㅋㅋㅋㅋ
#
##print("""n e
##- -----------
##0 1
##1 2
##2 2.5
##3 2.666666667
##4 2.708333333
##5 2.716666667
##6 2.718055556
##7 2.718253968
##8 2.718278770
##9 2.718281526""")
