# 1977

# if (complete): #를 사용하면 len() 안써도 되어서 코드가 조금 짧아질 수 있다.

import math

low = int(input())
up = int(input())

lower = math.ceil(math.sqrt(low))
upper = math.floor(math.sqrt(up))

complete = []
for num in range(lower, upper + 1):
    complete.append(num ** 2)

if (len(complete) == 0):
    print(-1)
else:
    print(sum(complete))
    print(min(complete))
