# 5666

# ans = int((H/P)*100 + 0.5)/100
# print(f'{ans:.2f}')
# 이런식으로 하면 자릿수 지정 가능한가보다.

import sys

while (1):
    inp = sys.stdin.readline().rstrip()
    if (inp == ""):
        break

    h, p = map(int, inp.split())
    print('%.2f' %(round(h/p, 2)))
