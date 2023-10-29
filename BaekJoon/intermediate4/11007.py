# 11007

# insert 사용 대신, former_list에서 pop을 하고, new_list = [one] + former_list 하는 방법도 있다.

# 굳이 result 안만들고 end=""으로 바로바로 print하는 방법도 있다.

import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    number = list(map(int, sys.stdin.readline().split()))

    alpha = [chr(x) for x in range(97, 123)]
    result = ""
    for want in number:
        tmp = alpha.pop(want)
        alpha.insert(0, tmp)
        result += tmp

    print(result)
