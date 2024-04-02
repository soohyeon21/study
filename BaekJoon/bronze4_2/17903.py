# 17903

# 무언가 한가득 적혀있기는 하지만, 결국에는 입력받은 m의 수에 따라 출력을 결정해주면 된다.
# m, n을 입력받은 후의 나머지 입력은 코드에서 입력받도록 처리하지 않아도 되나 보다.

import sys

m, n = map(int, sys.stdin.readline().split())

for _ in range(m):
    variables = map(int, sys.stdin.readline().split())

if (m >= 8):
    print("satisfactory")
else:
    print("unsatisfactory")
