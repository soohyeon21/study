# 17009

# 방법은 여러가지이나, 어떻게 작성한 코드가 좋은 코드인 것인가.

import sys

apples = 0
bananas = 0
score = [3, 2, 1]

for i in range(3):
    plus = int(sys.stdin.readline())
    apples += plus * score[i]

for i in range(3):
    plus = int(sys.stdin.readline())
    bananas += plus * score[i]

if (apples > bananas):
    print("A")
elif (apples < bananas):
    print("B")
else:
    print("T")
